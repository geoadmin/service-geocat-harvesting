import os
import requests
import json
import logging
import datetime

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def upload_md(
    GEOCAT_USERNAME,
    GEOCAT_PASSWORD,
    PATH_TO_XML_FILES,
    API_URL,
    PARAMETER_UUID_PROCESSING,
    PARAMETER_GROUP,
    PARAMETER_REJECT_IF_INVALID,
    PARAMETER_PUBLISH_TO_ALL,
    UPDATE_DATE_STAMP
):
    session = requests.Session()
    session.auth = (GEOCAT_USERNAME, GEOCAT_PASSWORD)

    http_proxy = os.environ.get("HTTP_PROXY")
    https_proxy = os.environ.get("HTTPS_PROXY")
    if http_proxy or https_proxy:
        session.proxies.update({
            "http": http_proxy or "",
            "https": https_proxy or ""
        })
        logging.info(f"Using proxies: {session.proxies}")

    try:
        response = session.get(f"{API_URL}/me", headers={"accept": "application/json"})
        response.raise_for_status()
        xsrf_token = response.cookies.get("XSRF-TOKEN")
        session.headers.update({
            "X-XSRF-TOKEN": xsrf_token,
            "accept": "application/json"
        })
        logging.info("Authenticated successfully.")
    except Exception as e:
        logging.error(f"Authentication failed: {e}")
        if response is not None:
            logging.error(f"Response content: {response.content}")
        return

    xml_files = [
        os.path.join(PATH_TO_XML_FILES, f)
        for f in os.listdir(PATH_TO_XML_FILES)
        if f.lower().endswith('.xml')
    ]

    if not xml_files:
        logging.warning("No XML files found in the directory.")
        return

    for xml_file in xml_files:
        logging.info(f"Uploading XML: {xml_file}")
        try:
            with open(xml_file, 'rb') as f:
                response = session.post(
                    f"{API_URL}/records",
                    files={'file': (xml_file, f, 'text/xml')},
                    params={
                        'metadataType': 'METADATA',
                        'uuidProcessing': PARAMETER_UUID_PROCESSING,
                        'group': PARAMETER_GROUP,
                        'rejectIfInvalid': PARAMETER_REJECT_IF_INVALID,
                        'publishToAll': PARAMETER_PUBLISH_TO_ALL,
                        'changeDate': 'now',
                    }
                )
                response.raise_for_status()
                upload_response = response.json()
                logging.info(f"Upload response: {json.dumps(upload_response, indent=2)}")

                if UPDATE_DATE_STAMP:
                    metadata_infos = upload_response.get('metadataInfos', {})
                    if not metadata_infos:
                        logging.warning("No metadataInfos in upload response, skipping date update")
                        continue
                    
                    first_group = next(iter(metadata_infos.values()), None)
                    if not first_group or not first_group[0]:
                        logging.warning("No metadata group found, skipping date update")
                        continue
                    
                    uuid = first_group[0].get('uuid')
                    if not uuid:
                        logging.warning("No UUID found in metadata group, skipping date update")
                        continue
                    
                    now_iso = datetime.datetime.now().isoformat(timespec='seconds')

                    update_url = f"{API_URL}/records/batchediting"
                    params = {
                        "uuids": uuid,
                        "updateDateStamp": "true"
                    }
                    payload = [
                        {
                        "xpath": ".//gmd:identificationInfo//gmd:citation//gmd:date/*[gmd:dateType/*/@codeListValue='revision']/gmd:date/gco:DateTime",
                        "value": now_iso,
                        "condition": ""
                        }
                    ]
                    
                    response = session.put(
                        update_url,
                        params=params,
                        json=payload
                    )
                    response.raise_for_status()
                    logging.info(f"Successfully updated dateStamp for UUID {uuid} with value {now_iso}")
                else:
                    logging.info("UPDATE_DATE_STAMP is False, skipping date update")
                
        except Exception as e:
            logging.error(f"Error processing {xml_file}: {e}")
            if 'response' in locals():
                logging.error(f"Response content: {response.content}")