# 🚀 Erste Schritte

Willkommen! Dieses Handbuch hilft Ihnen, das geocat harvesting tool von Grund auf einzurichten.

---

## 1️⃣ Python installieren

Dieses Projekt benötigt **Python 3.8 oder höher**.

- [Python herunterladen](https://www.python.org/downloads/)
- Unter Linux:
    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```
- Unter Windows: Laden Sie den Installer herunter, führen Sie ihn aus und aktivieren Sie „Add Python to PATH“.

---

## 2️⃣ Tool herunterladen

**Wenn Sie mit git vertraut sind:**
```sh
git clone https://github.com/geoadmin/service-geocat-harvesting.git
cd service-geocat-harvesting
```
**Falls nicht:**  
- Gehen Sie zum [GitHub-Repository](https://github.com/geoadmin/service-geocat-harvesting)
- Klicken Sie auf **Code > Download ZIP**
- Entpacken Sie die ZIP-Datei und öffnen Sie den Ordner

---

## 3️⃣ Abhängigkeiten installieren

Sie benötigen folgende Python-Pakete:
- [`requests`](https://pypi.org/project/requests/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Installieren Sie diese mit (wählen Sie den passenden Befehl):

```sh
pip install requests python-dotenv
# oder, falls Sie Python 3 verwenden:
pip3 install requests python-dotenv
# oder, unter Windows:
py -m pip install requests python-dotenv
# oder, falls Sie eine virtuelle Umgebung nutzen, aktivieren Sie diese zuerst!
```

> **💡 Falls Sie eine Fehlermeldung „command not found“ erhalten, probieren Sie `pip3` oder `py -m pip` statt `pip`.  
> Aktivieren Sie Ihre virtuelle Umgebung vor der Installation.**

---

## 4️⃣ Umgebung konfigurieren

### a. `.env`-Datei erstellen

Kopieren Sie das Beispiel und bearbeiten Sie es:

```sh
cp .env.example .env
notepad .env   # (Windows)
nano .env      # (Linux/Mac)
```

Tragen Sie Ihre geocat.ch-Zugangsdaten ein:

```ini
GEOCAT_USERNAME=ihr_benutzername
GEOCAT_PASSWORD=ihr_passwort
```

### b. `config.py` bearbeiten

Öffnen Sie `config.py` und passen Sie die notwendigen Parameter an:

```python
# API-Endpunkt
API_URL = "https://geocat.ch/api"

# Zielgruppen-ID (muss zu Ihrer Gruppe passen)
PARAMETER_GROUP = 42

# Metadaten-Verarbeitungsoptionen
PARAMETER_UUID_PROCESSING = "OVERWRITE"
UPDATE_DATE_STAMP = True

# Validierungsstrenge
REJECT_IF_INVALID = True
```

- **PARAMETER_GROUP**: Verwenden Sie die Ihrer Organisation zugewiesene Gruppen-ID.
- **UPDATE_DATE_STAMP**: Setzen Sie auf `True`, um das Revisionsdatum nach dem Upload zu aktualisieren.

Weitere Details finden Sie unter [Parameter](parameters.md).

### c. (Optional) Proxy konfigurieren

Falls Sie sich hinter einem Proxy befinden (z.B. in einer Behörde oder Firma), setzen Sie vor dem Start des Skripts diese Umgebungsvariablen:

- **Unter Linux/Mac:**
    ```sh
    export HTTP_PROXY="http://proxy.beispiel.de:8080"
    export HTTPS_PROXY="http://proxy.beispiel.de:8080"
    python main.py
    ```

- **Unter Windows (cmd):**
    ```bat
    set HTTP_PROXY=http://proxy.beispiel.de:8080
    set HTTPS_PROXY=http://proxy.beispiel.de:8080
    python main.py
    ```

Sie können diese Variablen auch in Ihre `.env`-Datei eintragen:

```ini
HTTP_PROXY=http://proxy.beispiel.de:8080
HTTPS_PROXY=http://proxy.beispiel.de:8080
```

Das Skript verwendet diese Proxy-Einstellungen automatisch.

---

## 5️⃣ XML-Dateien ablegen

Legen Sie alle Ihre Metadaten-XML-Dateien in den Ordner, der in `config.py` unter `PATH_TO_XML_FILES` angegeben ist.

---

## 6️⃣ Skript ausführen

- **Unter Windows:**
  1. Öffnen Sie den Ordner, in dem Sie das Projekt extrahiert/geklohnt haben.
  2. Halten Sie `Shift` gedrückt und klicken Sie mit der rechten Maustaste in den Ordner. Wählen Sie „PowerShell-Fenster hier öffnen“ oder „Eingabeaufforderung hier öffnen“.
  3. Geben Sie ein:
     ```sh
     python main.py
     ```

- **Unter Linux/Mac:**
  1. Öffnen Sie ein Terminal.
  2. Navigieren Sie mit `cd` in den Projektordner.
  3. Führen Sie aus:
     ```sh
     python3 main.py
     ```

- **Sie können das Skript auch mit Visual Studio Code oder einer anderen IDE ausführen**

Sie sollten eine Ausgabe wie diese sehen:
```
[INFO] 5 Dateien erfolgreich hochgeladen
```

---

## 📝 Tipps & Best Practices

- **Verwenden Sie eine virtuelle Umgebung**, um Abhängigkeitskonflikte zu vermeiden:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
- **Überprüfen Sie Ihre Logs** nach jedem Lauf auf Fehler oder Warnungen.
- **Automatisieren Sie Ihre Uploads** mit [cron](automation.md#🐧-linux-cron) (Linux) oder [Task Scheduler](automation.md#🪟-windows-task-scheduler) (Windows).

---

Weitere Hilfe finden Sie in den Abschnitten [Automatisierung](automation.md) und [Parameter](parameters.md) oder eröffnen Sie ein Issue auf [GitHub](https://github.com/geoadmin/service-geocat-harvesting/issues).