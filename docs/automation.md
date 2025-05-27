# 🤖 Automation

## 🐧 Linux (cron)

```sh
crontab -e
```
Add for example:
```sh
0 * * * * /usr/bin/python3 /path/to/main.py >> /var/log/geocat.log 2>&1
```
Restart cron if needed:
```sh
service cron restart
```

---

## 🪟 Windows (Task Scheduler)

1. Open **Task Scheduler**
2. Create a **Basic Task**
3. Set the **Trigger** (Daily/Hourly)
4. **Action**: "Start a program"
    - **Program**: `python.exe`
    - **Arguments**: `main.py`
    - (Set the "Start in" directory if needed)

---

## 📈 Monitoring

| Log File              | Purpose                  |
|-----------------------|--------------------------|
| `/var/log/geocat.log` | All output and errors    |
| `errors.log`          | Critical errors only     |

To monitor logs in real time:
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