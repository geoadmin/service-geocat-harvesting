# 🐱 geocat harvesting tool

> **Automatisieren Sie Ihre Metadaten-Uploads zu [geocat.ch](https://www.geocat.ch/) ganz einfach!**

---

## 🌍 Was ist Harvesting?

**Harvesting** ist der Prozess des automatischen Sammelns und Hochladens von Metadaten (XML-Dateien) in den geocat.ch-Katalog.  
Dieses Tool hilft Ihnen, Metadaten stapelweise hochzuladen, zu aktualisieren und zu planen – das spart Zeit und reduziert Fehler.

---

## 🚦 Wie benutze ich dieses Tool? (3 einfache Schritte)

### 1️⃣ Einrichtung & Installation

- Installieren Sie Python 3.8+ und die benötigten Abhängigkeiten.
- Klonen Sie das Repository und installieren Sie die Python-Pakete.

[🛠️ Erste Schritte ansehen](getting-started.md)

---

### 2️⃣ Passen Sie Ihre Parameter an

- Konfigurieren Sie Ihre Zugangsdaten und API-Einstellungen in `.env` und `config.py`.
- Legen Sie Ihre Zielgruppe, Verarbeitungsoptionen und den Ordner mit Ihren XML-Dateien fest.

[⚙️ Alle Parameter ansehen](parameters.md)

---

### 3️⃣ Automatisieren Sie Ihre Uploads

- Planen Sie das Skript zur automatischen Ausführung mit **cron** (Linux) oder dem **Task Scheduler** (Windows).
- Überwachen Sie Ihre Logs, um sicherzustellen, dass alles reibungslos läuft.

[🤖 Automatisierungsanleitung](automation.md)

---

## 📝 Kurzes Beispiel

```sh
python main.py --path ./metadata --group 42
# Ausgabe:
# 12 Metadatensätze erfolgreich hochgeladen
```