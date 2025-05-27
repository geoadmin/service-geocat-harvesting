# 🚦 Getting Started

## 🖥️ Requirements

- Python 3.8+
- A geocat.ch user account with write permissions on the target group.
- Python dependencies: `requests`, `python-dotenv`

---

## ⚡ Installation

1. 📥 **Clone the repository or copy the files into a folder.**
2. 📦 **Install dependencies:**
   ```sh
   pip install requests python-dotenv
   ```
3. 🛠️ **Configure your credentials:**
   - Create a `.env` file with:
     ```
     GEOCAT_USERNAME=your_username
     GEOCAT_PASSWORD=your_password
     ```
   - Edit `config.py` to set your XML folder and other parameters.

[➡️ See all parameters and how to configure them](parameters.md)

4. 📁 **Place your XML files in the folder specified by `PATH_TO_XML_FILES`.**

---

## ▶️ Usage

Run the script with:

```sh
python main.py
```

The script will:
- Check if the XML folder exists.
- Authenticate to geocat.ch.
- ⬆Upload each XML file.
- Optionally update the revision date.

---

For advanced configuration and automation, see the [main documentation](index.md).
