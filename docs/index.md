# 🐱 geocat harvesting tool

> **Automate your metadata uploads to [geocat.ch](https://www.geocat.ch/) with ease!**

---

## 🌍 What is harvesting?

**Harvesting** is the process of automatically collecting and uploading metadata records (XML files) to the geocat.ch catalog.  
This tool helps you batch-upload, update, and schedule your metadata management, saving you time and reducing errors.

---

## 🚦 How to use this tool? (3 easy steps)

### 1️⃣ Setup & Installation

- Install Python 3.8+ and required dependencies.
- Clone the repository and install Python packages.

[🛠️ See Getting Started](getting-started.md)

---

### 2️⃣ Adjust your parameters

- Configure your credentials and API settings in `.env` and `config.py`.
- Set your target group, processing options, and the folder containing your XML files.

[⚙️ See all parameters](parameters.md)

---

### 3️⃣ Automate your uploads

- Schedule the script to run automatically using **cron** (Linux) or **Task Scheduler** (Windows).
- Monitor your logs to ensure everything runs smoothly.

[🤖 Automation guide](automation.md)

---

## 📝 Quick Example

```sh
python [main.py](http://_vscodecontentref_/1) --path ./metadata --group 42
# Output:
# Successfully uploaded 12 metadata records
```