from upload_md import upload_md
import config
import os
import sys

def main():
    # Vérifie que le dossier existe
    if not os.path.isdir(config.PATH_TO_XML_FILES):
        print(f"Erreur : le dossier {config.PATH_TO_XML_FILES} n'existe pas.")
        sys.exit(1)

    try:
        upload_md(
            config.GEOCAT_USERNAME,
            config.GEOCAT_PASSWORD,
            config.PATH_TO_XML_FILES,
            config.API_URL,
            config.PARAMETER_UUID_PROCESSING,
            str(config.PARAMETER_GROUP),
            config.PARAMETER_REJECT_IF_INVALID,
            config.PARAMETER_PUBLISH_TO_ALL,
            config.UPDATE_DATE_STAMP
        )
        print("Upload completed.")
    except Exception as e:
        print(f"Error during upload: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()