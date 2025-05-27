# 🚀 geocat Harvesting Script

This project automates the upload of XML metadata files to the [geocat.ch](https://www.geocat.ch/) (GeoNetwork) API and optionally updates their revision date.

<br>

[▶️ Getting started](getting-started.md)  
[⚙️ Parameters](parameters.md)  
[🤖 Automation](automation.md)

---

## ✨ Features

- Authenticates to the geocat API using username and password.
- Automatically uploads all `.xml` files from a specified folder to the API.
- Optionally updates the `dateStamp` field of the metadata after upload.
- Detailed logging of operations and errors.

---

<p align="left">
  <a href="getting-started.md#️-requirements" style="background:#0366d6;color:white;padding:8px 16px;border-radius:4px;text-decoration:none;font-weight:bold;">🖥️ Requirements</a>
  &nbsp;
  <a href="getting-started.md#️-installation" style="background:#28a745;color:white;padding:8px 16px;border-radius:4px;text-decoration:none;font-weight:bold;">⚡ Installation</a>
  &nbsp;
  <a href="getting-started.md#️-usage" style="background:#6f42c1;color:white;padding:8px 16px;border-radius:4px;text-decoration:none;font-weight:bold;">▶️ Usage</a>
</p>

---

## 🛠️ Customization

- 🎯 **Target group**: edit `PARAMETER_GROUP` in `config.py`.
- ⚙️ **Upload parameters**: adjust other variables in `config.py` as needed.

---

## 🗂️ Project Structure

```
.
├── main.py
├── upload_md.py
├── config.py
├── .env
└── [XML folder]
```

---

## 📋 Logging

Logs are displayed in the console. To redirect them to a file, run:

```sh
python main.py >> log.txt 2>&1
```

---

## 👥 Authors

Script adapted and automated for geocat.ch by swisstopo.

---

> **ℹ️ Note:**  
> This script updates the `dateStamp` field of each metadata record after upload if the option is enabled.  
> Make sure your user has the necessary permissions on the target group.