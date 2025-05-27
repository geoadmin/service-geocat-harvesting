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

```python
# API endpoint
API_URL = "https://geocat.ch/api"

# Target group ID (must match your group permissions)
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
See [`config.py`](../config.py) for more details and default values.