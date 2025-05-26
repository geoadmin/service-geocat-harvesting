import os
from dotenv import load_dotenv

load_dotenv()

GEOCAT_USERNAME = os.getenv('GEOCAT_USERNAME')
GEOCAT_PASSWORD = os.getenv('GEOCAT_PASSWORD')
API_URL = 'https://geocat-int.dev.bgdi.ch/geonetwork/srv/api'
PARAMETER_UUID_PROCESSING = 'OVERWRITE'
PARAMETER_GROUP = 00000  # Replace with the actual group number
PARAMETER_REJECT_IF_INVALID = 'true'
PARAMETER_PUBLISH_TO_ALL = 'true'
PATH_TO_XML_FILES = os.path.expanduser('path/to/xmls/folder')  # Update this path to your XML files