# geocat Harvesting Script

This project automates the upload of XML metadata records to the geocat.ch (GeoNetwork) API and optionally updates their DateStamp (last update of the metadata record).

## Features

- Authenticates to the geocat API using username and password.
- Automatically uploads all `.xml` files from a specified folder to the API.
- Optionally updates the `dateStamp` field of the metadata after upload.
- Detailed logging of operations and errors.

## Requirements

- Python 3.8+
- A geocat.ch user account with write permissions on the target group.
- Python dependencies:
  - `requests`
  - `python-dotenv` (if you use a `.env` file for credentials)

## Installation

1. **Clone the repository or copy the files into a folder.**

2. **Install dependencies:**
   ```sh
   pip install requests python-dotenv
   ```

3. **Configure parameters in `config.py` and `.env`:**
   - `.env`:
     ```
     GEOCAT_USERNAME=your_username
     GEOCAT_PASSWORD=your_password
     ```
   - `config.py`: adjust paths, group, and other parameters as needed.

4. **Place your XML files to upload in the folder defined by `PATH_TO_XML_FILES` in `config.py`.**

## Usage

Simply run:

```sh
python main.py
```

The script will:
- Check if the XML folder exists.
- Authenticate the user.
- Upload each XML file.
- Update the revision date if `UPDATE_DATE_STAMP` is set to `True`.

## Automation

### On Linux

Use `cron` to run the script at regular intervals:

```sh
crontab -e
```
Add for example:
```
0 * * * * /usr/bin/python3 /path/to/main.py >> /path/to/cron.log 2>&1
```

### On Windows

Use the **Task Scheduler** to run the script automatically (see Windows documentation).

## Customization

- **Target group**: edit `PARAMETER_GROUP` in `config.py`.
- **Upload parameters**: adjust other variables in `config.py` as needed.

## Project Structure

```
.
├── main.py
├── upload_md.py
├── config.py
├── .env
└── [XML folder]
```

## Logging

Logs are displayed in the console. To redirect them to a file, run:

```sh
python main.py >> log.txt 2>&1
```

## Authors

Script adapted and automated for geocat.ch by swisstopo.

---

**Note:**  
This script updates the `dateStamp` field of each metadata record after upload if the option is enabled.  
Make sure your user has the necessary permissions on the target group.
