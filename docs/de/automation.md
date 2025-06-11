# 🤖 Automatisierung

Automatisieren Sie Ihre Metadaten-Uploads, damit Sie keinen Batch mehr vergessen!

---

## 🐧 Linux (cron)

Planen Sie das Skript zur automatischen Ausführung mit `cron`.

1. Crontab bearbeiten:
    ```sh
    crontab -e
    ```
2. Fügen Sie eine Zeile hinzu, um das Skript stündlich auszuführen (Pfad anpassen!):
    ```sh
    0 * * * * /usr/bin/python3 /pfad/zu/main.py >> /var/log/geocat.log 2>&1
    ```
    - `0 * * * *` = jede volle Stunde
    - `/usr/bin/python3` und `/pfad/zu/main.py` entsprechend anpassen

3. Cron ggf. neu starten:
    ```sh
    sudo service cron restart
    ```

---

## 🪟 Windows (Task Scheduler)

Automatisieren Sie das Skript unter Windows mit dem Task Scheduler:

1. Öffnen Sie den **Task Scheduler** über das Startmenü.
2. Erstellen Sie eine **Basic Task**.
3. Legen Sie den **Trigger** fest (z.B. täglich, stündlich).
4. Für **Action** wählen Sie "Programm starten":
    - **Programm/Skript**: `python.exe`
    - **Argumente hinzufügen**: `C:\Pfad\zu\main.py`
    - **Starten in**: `C:\Pfad\zu\Ihrem\Projektordner` (optional, empfohlen)
5. Aufgabe abschliessen und aktivieren.

> 💡 Falls Sie eine virtuelle Umgebung nutzen, geben Sie den Python-Pfad innerhalb von `venv\Scripts\python.exe` an.

---

## 📈 Überwachung & Logs

| Logdatei                | Zweck                    |
|-------------------------|--------------------------|
| `/var/log/geocat.log`   | Alle Ausgaben und Fehler |
| `errors.log`            | Nur kritische Fehler     |

Logs in Echtzeit überwachen (Linux):
```sh
tail -f /var/log/geocat.log
```

Beispielausgabe:
```
[INFO] 2023-06-01 10:00: - Verarbeitung von 3 neuen Dateien
```

---

!!! tip "Profi-Tipp"
    Testen Sie Ihre Automatisierung zuerst mit einem Testlauf:
    ```sh
    python main.py --dry-run
    ```

---

**Brauchen Sie Hilfe?**  
Siehe die Abschnitte [Getting Started](getting-started.md) und [Parameters](parameters.md) oder eröffnen Sie ein Issue auf [GitHub](https://github.com/geoadmin/service-geocat-harvesting/issues).