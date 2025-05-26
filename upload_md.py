import os
import requests
import json
import logging

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
    PARAMETER_PUBLISH_TO_ALL
):
    session = requests.Session()
    session.auth = (GEOCAT_USERNAME, GEOCAT_PASSWORD)

    try:
        # Authentification AVEC session et auth
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
                logging.info(f"Upload response: {json.dumps(response.json(), indent=2)}")
        except Exception as e:
            logging.error(f"Error uploading {xml_file}: {e}")
            if response is not None:
                logging.error(f"Response content: {response.content}")