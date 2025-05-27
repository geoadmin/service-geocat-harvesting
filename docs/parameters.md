# ⚙️ Parameters

All parameters are set in `config.py` and `.env`:

| Parameter                   | Where         | Description                                                                 | Example/Default                                      |
|-----------------------------|--------------|-----------------------------------------------------------------------------|------------------------------------------------------|
| `GEOCAT_USERNAME`           | `.env`       | Your geocat.ch username                                                     | `GEOCAT_USERNAME=your_username`                      |
| `GEOCAT_PASSWORD`           | `.env`       | Your geocat.ch password                                                     | `GEOCAT_PASSWORD=your_password`                      |
| `API_URL`                   | `config.py`  | Geocat API endpoint                                                         | `'https://geocat-int.dev.bgdi.ch/geonetwork/srv/api'`|
| `PARAMETER_UUID_PROCESSING` | `config.py`  | How to handle UUIDs (`GENERATEUUID`, `OVERWRITE`, etc.)                     | `'OVERWRITE'`                                        |
| `PARAMETER_GROUP`           | `config.py`  | Target group ID for upload                                                  | `42`                                                 |
| `PARAMETER_REJECT_IF_INVALID`| `config.py` | Reject invalid metadata (`true`/`false`)                                    | `'true'`                                             |
| `PARAMETER_PUBLISH_TO_ALL`  | `config.py`  | Publish to all (`true`/`false`)                                             | `'true'`                                             |
| `PATH_TO_XML_FILES`         | `config.py`  | Path to the folder containing your XML files                                | `'/home/cuo/Projets/service-geocat-harvesting'`      |
| `UPDATE_DATE_STAMP`         | `config.py`  | Set to `True` to update the `dateStamp` after upload                        | `True`                                               |

**Tip:**  
See [config.py](../config.py) for more details and default values.