# 🚀 Getting Started

Welcome! This guide will help you set up the geocat harvesting tool from scratch.

---

## 1️⃣ Install Python

This project requires **Python 3.8 or higher**.

- [Download Python](https://www.python.org/downloads/)
- On Linux:
    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```
- On Windows: download and run the installer, and make sure to check “Add Python to PATH”.

---

## 2️⃣ Get the tool

**If you are comfortable with git:**
```sh
git clone https://github.com/geoadmin/service-geocat-harvesting.git
cd service-geocat-harvesting
```
**If not:**  
- Go to [the GitHub repository](https://github.com/geoadmin/service-geocat-harvesting)
- Click **Code > Download ZIP**
- Extract the ZIP and open the folder

---

## 3️⃣ Install dependencies

You need the following Python packages:
- [`requests`](https://pypi.org/project/requests/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Install them with (choose the command that works for your system):

```sh
pip install requests python-dotenv
# or, if you use Python 3:
pip3 install requests python-dotenv
# or, if you use Windows:
py -m pip install requests python-dotenv
# or, if you use a virtual environment, activate it first!
```

> **💡 If you get a "command not found" error, try `pip3` or `py -m pip` instead of `pip`.  
> If you use a virtual environment, activate it before installing.**

---

## 4️⃣ Configure your environment

### a. Create your `.env` file

Copy the example and edit it:

```sh
cp .env.example .env
notepad .env   # (Windows)
nano .env      # (Linux/Mac)
```

Fill in your geocat.ch credentials:

```ini
GEOCAT_USERNAME=your_username
GEOCAT_PASSWORD=your_password
```

### b. Edit `config.py`

Open `config.py` and set the required parameters:

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

- **PARAMETER_GROUP**: Use the group ID assigned to your organization.
- **UPDATE_DATE_STAMP**: Set to `True` to update the revision date after upload.

For more details, see [Parameters](parameters.md).

### c. (Optional) Configuring a Proxy

If you are behind a proxy (e.g. in a corporate or government network), set these environment variables before running the script:

- **On Linux/Mac:**
    ```sh
    export HTTP_PROXY="http://proxy.example.com:8080"
    export HTTPS_PROXY="http://proxy.example.com:8080"
    python main.py
    ```

- **On Windows (cmd):**
    ```bat
    set HTTP_PROXY=http://proxy.example.com:8080
    set HTTPS_PROXY=http://proxy.example.com:8080
    python main.py
    ```

You can also add these variables to your `.env` file:

```ini
HTTP_PROXY=http://proxy.example.com:8080
HTTPS_PROXY=http://proxy.example.com:8080
```

The script will automatically use these proxy settings.

---

## 5️⃣ Place your XML files

Put all your metadata XML files in the folder specified by `PATH_TO_XML_FILES` in `config.py`.

---

## 6️⃣ How to run the script

- **On Windows:**
  1. Open the folder where you extracted/cloned the project.
  2. Hold `Shift` and right-click in the folder, then choose “Open PowerShell window here” or “Open command window here”.
  3. Type:
     ```sh
     python main.py
     ```

- **On Linux/Mac:**
  1. Open a terminal.
  2. `cd` into the project folder.
  3. Run:
     ```sh
     python3 main.py
     ```

- **You can also use Visual Studio Code or another IDE to run the script**

You should see output like:
```
[INFO] Uploaded 5 files successfully
```

---

## 📝 Tips & Best Practices

- **Use a virtual environment** to avoid dependency conflicts:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
- **Check your logs** for errors or warnings after each run.
- **Automate** your uploads with [cron](automation.md#🐧-linux-cron) (Linux) or [Task Scheduler](automation.md#🪟-windows-task-scheduler) (Windows).

---

For more help, see the [Automation](automation.md) and [Parameters](parameters.md) sections, or open an issue on [GitHub](https://github.com/geoadmin/service-geocat-harvesting/issues).