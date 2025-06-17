from config import *
from upload_md import upload_md
import config
import os
import sys

def main():
    if not os.path.isdir(config.PATH_TO_XML_FILES):
        print(f"❓ Error: Folder {config.PATH_TO_XML_FILES} doesn't exist.")
        sys.exit(1)
    try:
        upload_md(
            GEOCAT_USERNAME,
            GEOCAT_PASSWORD,
            PATH_TO_XML_FILES,
            API_URL,
            PARAMETER_UUID_PROCESSING,
            PARAMETER_GROUP,
            PARAMETER_REJECT_IF_INVALID,
            PARAMETER_PUBLISH_TO_ALL,
            UPDATE_DATE_STAMP,
            PROXY_HTTP,
            PROXY_HTTPS
        )
        print("Upload completed.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()