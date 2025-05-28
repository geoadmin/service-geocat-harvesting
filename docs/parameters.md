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

| Variable            | Required | Description             |
|---------------------|----------|-------------------------|
| `GEOCAT_USERNAME`   | Yes      |  |
| `GEOCAT_PASSWORD`   | Yes      | Your geocat.ch password |
| `API_URL`   | Yes      | url of the api. For Production: "https://www.geocat.ch/geonetwork/srv/api/" |
| `PARAMETER_GROUP`   | Yes      | Group ID of your organisation (42 for Freiburg for example) |
| `PARAMETER_UUID_PROCESSING`   | Yes      | Several options in case of uuid conflict: <br>- 'GENERATEUUID': create a new uuid for uploaded metadata records <br>- 'OVERWRITE': deletes the old metadata record with the same uuid and adds the new one <br>-'NOTHING': does nothing, record not uploaded  |
| `REJECT_IF_INVALID`   | Yes      | If "True", accept metadata records not valid, if "False", only metadata records with valid schema is accepted |
| `UPDATE_DATE_STAMP`   | Yes      | If true, update the metadata date stamp |


Example:
```python
# API endpoint
API_URL = "https://geocat.ch/api"

# Target group ID (must match your group)
PARAMETER_GROUP = 42

# Metadata processing options
PARAMETER_UUID_PROCESSING = "OVERWRITE"
UPDATE_DATE_STAMP = True

# Validation strictness
REJECT_IF_INVALID = True
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