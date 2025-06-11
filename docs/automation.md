# 🤖 Automation

Automate your metadata uploads so you never forget a batch!

---

## 🐧 Linux (cron)

Schedule the script to run automatically at regular intervals using `cron`.

1. Edit your crontab:
    ```sh
    crontab -e
    ```
2. Add a line to run the script every hour (adapt the path as needed):
    ```sh
    0 * * * * /usr/bin/python3 /path/to/main.py >> /var/log/geocat.log 2>&1
    ```
    - `0 * * * *` = every hour on the hour
    - Change `/usr/bin/python3` and `/path/to/main.py` to your actual paths

3. Restart cron if needed:
    ```sh
    sudo service cron restart
    ```

---

## 🪟 Windows (Task Scheduler)

Automate the script on Windows using Task Scheduler:

1. Open **Task Scheduler** from the Start menu.
2. Create a **Basic Task**.
3. Set the **Trigger** (e.g., daily, hourly).
4. For **Action**, choose "Start a program":
    - **Program/script**: `python.exe`
    - **Add arguments**: `C:\path\to\main.py`
    - **Start in**: `C:\path\to\your\project\folder` (optional but recommended)
5. Finish and enable the task.

> 💡 If you use a virtual environment, point to the Python executable inside your `venv\Scripts\python.exe`.

---

## 📈 Monitoring & Logs

| Log File              | Purpose                  |
|-----------------------|--------------------------|
| `/var/log/geocat.log` | All output and errors    |
| `errors.log`          | Critical errors only     |

Monitor logs in real time (Linux):
```sh
tail -f /var/log/geocat.log
```

Example output:
```
[INFO] 2023-06-01 10:00: - Processing 3 new files
```

---

!!! tip "Pro Tip"
    Test your automation with a dry run first:
    ```sh
    python main.py --dry-run
    ```

---

**Need help?**  
Check the [Getting Started](getting-started.md) and [Parameters](parameters.md) sections, or open an issue on [GitHub](https://github.com/geoadmin/service-geocat-harvesting/issues).