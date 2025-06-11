# ⚙️ Configuration Parameters

## 🌱 Environment Variables (`.env`)

| Variable            | Required | Description             |
|---------------------|----------|-------------------------|
| `GEOCAT_USERNAME`   | Yes      | Your geocat.ch username |
| `GEOCAT_PASSWORD`   | Yes      | Your geocat.ch password |

Example:
```ini
# .env
GEOCAT_USERNAME=user@example.com
GEOCAT_PASSWORD=s3cr3t
```

---

## 🛠️ Script Configuration (`config.py`)

| Parameter                   | Required | Description                                                                                                    | Example/Default                                      |
|-----------------------------|----------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `API_URL`                   | Yes      | Geocat API endpoint                                                                                            | `"https://www.geocat.ch/geonetwork/srv/api/"`        |
| `PARAMETER_GROUP`           | Yes      | Target group ID for your organisation (e.g. 42 for Freiburg)                                                   | `42`                                                 |
| `PARAMETER_UUID_PROCESSING` | Yes      | What to do in case of UUID conflict:<br>- `GENERATEUUID`: create a new UUID<br>- `OVERWRITE`: replace existing<br>- `NOTHING`: skip upload | `"OVERWRITE"`                                        |
| `REJECT_IF_INVALID`         | Yes      | If `True`, accept invalid metadata; if `False`, only valid records are accepted                                | `True`                                               |
| `UPDATE_DATE_STAMP`         | Yes      | If `True`, update the metadata date stamp after upload                                                         | `True`                                               |
| `PARAMETER_PUBLISH_TO_ALL`  | No       | If `True`, publish to all (default: `False`)                                                                   | `False`                                              |
| `PATH_TO_XML_FILES`         | Yes      | Path to the folder containing your XML files                                                                   | `"./metadata"`                                       |

Example:
```python
# config.py
API_URL = "https://www.geocat.ch/geonetwork/srv/api/"
PARAMETER_GROUP = 42
PARAMETER_UUID_PROCESSING = "OVERWRITE"
REJECT_IF_INVALID = True
UPDATE_DATE_STAMP = True
PARAMETER_PUBLISH_TO_ALL = False
PATH_TO_XML_FILES = "./metadata"
```

---

## 🖥️ Command Line Options

You can also use command line options:

```sh
python main.py --help
```
Example output:
```
Usage: main.py [OPTIONS]
Options:
  --path TEXT      Path to XML files
  --group INTEGER  Target group ID
  --dry-run        Test without uploading
```

---

**Tip:**  
See [`config.py`](https://github.com/geoadmin/service-geocat-harvesting/blob/master/config.py) for more details and default values.