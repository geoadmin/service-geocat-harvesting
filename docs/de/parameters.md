# ⚙️ Konfigurationsparameter

## 🌱 Umgebungsvariablen (`.env`)

| Variable            | Erforderlich | Beschreibung                |
|---------------------|--------------|-----------------------------|
| `GEOCAT_USERNAME`   | Ja           | Ihr geocat.ch-Benutzername  |
| `GEOCAT_PASSWORD`   | Ja           | Ihr geocat.ch-Passwort      |

Beispiel:
```ini
# .env
GEOCAT_USERNAME=benutzer@example.com
GEOCAT_PASSWORD=geheim
```

---

## 🛠️ Skript-Konfiguration (`config.py`)

| Parameter                   | Erforderlich | Beschreibung                                                                                                    | Beispiel/Standardwert                                 |
|-----------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `API_URL`                   | Ja           | Geocat API-Endpunkt                                                                                             | `"https://www.geocat.ch/geonetwork/srv/api/"`         |
| `PARAMETER_GROUP`           | Ja           | Zielgruppen-ID Ihrer Organisation (z.B. 42 für Freiburg)                                                        | `42`                                                  |
| `PARAMETER_UUID_PROCESSING` | Ja           | Verhalten bei UUID-Konflikt:<br>- `GENERATEUUID`: Neue UUID erzeugen<br>- `OVERWRITE`: Bestehende ersetzen<br>- `NOTHING`: Upload überspringen | `"OVERWRITE"`                                         |
| `REJECT_IF_INVALID`         | Ja           | Wenn `True`, werden auch ungültige Metadaten akzeptiert; bei `False` nur gültige Datensätze                     | `True`                                                |
| `UPDATE_DATE_STAMP`         | Ja           | Wenn `True`, wird das Änderungsdatum nach dem Upload aktualisiert                                               | `True`                                                |
| `PARAMETER_PUBLISH_TO_ALL`  | Nein         | Wenn `True`, für alle veröffentlichen (Standard: `False`)                                                       | `False`                                               |
| `PATH_TO_XML_FILES`         | Ja           | Pfad zum Ordner mit Ihren XML-Dateien                                                                           | `"./metadata"`                                        |

Beispiel:
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

## 🖥️ Kommandozeilenoptionen

Sie können auch Kommandozeilenoptionen verwenden:

```sh
python main.py --help
```
Beispielausgabe:
```
Usage: main.py [OPTIONS]
Options:
  --path TEXT      Pfad zu den XML-Dateien
  --group INTEGER  Zielgruppen-ID
  --dry-run        Testlauf ohne Upload
```

---

**Tipp:**  
Siehe [`config.py`](https://github.com/geoadmin/service-geocat-harvesting/blob/master/config.py) für weitere Details und Standardwerte.