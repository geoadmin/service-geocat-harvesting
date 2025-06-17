import tkinter as tk
from tkinter import filedialog, messagebox
import config
import os
import subprocess
import sys

def save_config():
    with open("config.py", "w") as f:
        f.write(f"""import os
from dotenv import load_dotenv

load_dotenv()

GEOCAT_USERNAME = os.getenv('GEOCAT_USERNAME')
GEOCAT_PASSWORD = os.getenv('GEOCAT_PASSWORD')
API_URL = '{api_url.get()}'
PARAMETER_UUID_PROCESSING = '{uuid_processing.get()}'
PARAMETER_GROUP = {group.get()}
PARAMETER_REJECT_IF_INVALID = '{reject_invalid.get()}'
PARAMETER_PUBLISH_TO_ALL = '{publish_all.get()}'
PATH_TO_XML_FILES = os.path.expanduser(r'{xml_path.get()}')
UPDATE_DATE_STAMP = {update_date.get()}
""")
    with open(".env", "w") as f:
        f.write(f"GEOCAT_USERNAME={username.get()}\nGEOCAT_PASSWORD={password.get()}\n")
    messagebox.showinfo("Succès", "Configuration enregistrée !")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        xml_path.set(folder)

def run_script():
    save_config()
    # Lance main.py dans un terminal séparé
    try:
        if sys.platform.startswith('win'):
            subprocess.Popen(['python', 'main.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(['x-terminal-emulator', '-e', 'python3 main.py'])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lancer main.py : {e}")

root = tk.Tk()
root.title("geocat Config GUI")

username = tk.StringVar(value=config.GEOCAT_USERNAME)
password = tk.StringVar(value=config.GEOCAT_PASSWORD)
api_url = tk.StringVar(value=getattr(config, "API_URL", ""))
uuid_processing = tk.StringVar(value=getattr(config, "PARAMETER_UUID_PROCESSING", "OVERWRITE"))
group = tk.StringVar(value=getattr(config, "PARAMETER_GROUP", "42"))
reject_invalid = tk.StringVar(value=getattr(config, "PARAMETER_REJECT_IF_INVALID", "true"))
publish_all = tk.StringVar(value=getattr(config, "PARAMETER_PUBLISH_TO_ALL", "false"))
xml_path = tk.StringVar(value=getattr(config, "PATH_TO_XML_FILES", "./metadata"))
update_date = tk.StringVar(value=str(getattr(config, "UPDATE_DATE_STAMP", True)))

fields = [
    ("GEOCAT_USERNAME", username),
    ("GEOCAT_PASSWORD", password),
    ("API_URL", api_url),
    ("PARAMETER_UUID_PROCESSING", uuid_processing),
    ("PARAMETER_GROUP", group),
    ("PARAMETER_REJECT_IF_INVALID", reject_invalid),
    ("PARAMETER_PUBLISH_TO_ALL", publish_all),
    ("PATH_TO_XML_FILES", xml_path),
    ("UPDATE_DATE_STAMP", update_date),
]

for i, (label, var) in enumerate(fields):
    tk.Label(root, text=label).grid(row=i, column=0, sticky="e")
    if label == "GEOCAT_PASSWORD":
        tk.Entry(root, textvariable=var, show="*").grid(row=i, column=1)
    else:
        tk.Entry(root, textvariable=var).grid(row=i, column=1)
    if label == "PATH_TO_XML_FILES":
        tk.Button(root, text="Browse", command=browse_folder).grid(row=i, column=2)

tk.Button(root, text="Save Config", command=save_config).grid(row=len(fields), column=0, pady=10)
tk.Button(root, text="Run Script", command=run_script).grid(row=len(fields), column=1, pady=10)
tk.Button(root, text="Quit", command=root.quit).grid(row=len(fields), column=2, pady=10)

root.mainloop()