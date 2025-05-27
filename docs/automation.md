# 🤖 Automation

## On Linux

Use `cron` to run the script at regular intervals:

```sh
crontab -e
```
Add for example:
```
0 * * * * /usr/bin/python3 /path/to/main.py >> /path/to/cron.log 2>&1
```

## On Windows

Use the **Task Scheduler** to run the script automatically (see Windows documentation).

---