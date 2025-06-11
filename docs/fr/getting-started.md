# 🚀 Prise en main

Bienvenue ! Ce guide vous aide à configurer l’outil de récolte geocat depuis zéro.

---

## 1️⃣ Installer Python

Ce projet nécessite **Python 3.8 ou supérieur**.

- [Télécharger Python](https://www.python.org/downloads/)
- Sous Linux :
    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```
- Sous Windows : téléchargez et lancez l’installateur, et cochez “Add Python to PATH”.

---

## 2️⃣ Récupérer l’outil

**Si vous êtes à l’aise avec git :**
```sh
git clone https://github.com/geoadmin/service-geocat-harvesting.git
cd service-geocat-harvesting
```
**Sinon :**  
- Rendez-vous sur [le dépôt GitHub](https://github.com/geoadmin/service-geocat-harvesting)
- Cliquez sur **Code > Download ZIP**
- Décompressez le ZIP et ouvrez le dossier

---

## 3️⃣ Installer les dépendances

Vous avez besoin des paquets Python suivants :
- [`requests`](https://pypi.org/project/requests/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Installez-les avec (choisissez la commande adaptée à votre système) :

```sh
pip install requests python-dotenv
# ou, si vous utilisez Python 3 :
pip3 install requests python-dotenv
# ou, sous Windows :
py -m pip install requests python-dotenv
# ou, si vous utilisez un environnement virtuel, activez-le d’abord !
```

> **💡 Si vous obtenez une erreur "command not found", essayez `pip3` ou `py -m pip` à la place de `pip`.  
> Activez votre environnement virtuel avant d’installer.**

---

## 4️⃣ Configurer votre environnement

### a. Créer votre fichier `.env`

Copiez l’exemple et éditez-le :

```sh
cp .env.example .env
notepad .env   # (Windows)
nano .env      # (Linux/Mac)
```

Renseignez vos identifiants geocat.ch :

```ini
GEOCAT_USERNAME=votre_utilisateur
GEOCAT_PASSWORD=motdepasse
```

### b. Modifier `config.py`

Ouvrez `config.py` et ajustez les paramètres nécessaires :

```python
# URL de l’API
API_URL = "https://geocat.ch/api"

# ID du groupe cible (doit correspondre à votre groupe)
PARAMETER_GROUP = 42

# Options de traitement des métadonnées
PARAMETER_UUID_PROCESSING = "OVERWRITE"
UPDATE_DATE_STAMP = True

# Rigueur de validation
REJECT_IF_INVALID = True
```

- **PARAMETER_GROUP** : utilisez l’ID de groupe attribué à votre organisation.
- **UPDATE_DATE_STAMP** : mettez à `True` pour mettre à jour la date de révision après l’envoi.

Pour plus de détails, voir [Paramètres](parameters.md).

### c. (Optionnel) Configurer un proxy

Si vous êtes derrière un proxy (ex. en réseau d’entreprise ou administration), définissez ces variables d’environnement avant de lancer le script :

- **Sous Linux/Mac :**
    ```sh
    export HTTP_PROXY="http://proxy.exemple.com:8080"
    export HTTPS_PROXY="http://proxy.exemple.com:8080"
    python main.py
    ```

- **Sous Windows (cmd) :**
    ```bat
    set HTTP_PROXY=http://proxy.exemple.com:8080
    set HTTPS_PROXY=http://proxy.exemple.com:8080
    python main.py
    ```

Vous pouvez aussi ajouter ces variables dans votre fichier `.env` :

```ini
HTTP_PROXY=http://proxy.exemple.com:8080
HTTPS_PROXY=http://proxy.exemple.com:8080
```

Le script utilisera automatiquement ces paramètres proxy.

---

## 5️⃣ Placez vos fichiers XML

Placez tous vos fichiers XML de métadonnées dans le dossier indiqué par `PATH_TO_XML_FILES` dans `config.py`.

---

## 6️⃣ Lancer le script

- **Sous Windows :**
  1. Ouvrez le dossier où vous avez extrait/cloné le projet.
  2. Maintenez `Shift` et faites un clic droit dans le dossier, puis choisissez “Ouvrir une fenêtre PowerShell ici” ou “Ouvrir une fenêtre de commande ici”.
  3. Tapez :
     ```sh
     python main.py
     ```

- **Sous Linux/Mac :**
  1. Ouvrez un terminal.
  2. Faites `cd` dans le dossier du projet.
  3. Lancez :
     ```sh
     python3 main.py
     ```

- **Vous pouvez aussi utiliser Visual Studio Code ou un autre IDE pour lancer le script**

Vous devriez voir une sortie comme :
```
[INFO] 5 fichiers envoyés avec succès
```

---

## 📝 Conseils & bonnes pratiques

- **Utilisez un environnement virtuel** pour éviter les conflits de dépendances :
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
- **Vérifiez vos logs** après chaque exécution pour détecter erreurs ou avertissements.
- **Automatisez** vos envois avec [cron](automation.md#🐧-linux-cron) (Linux) ou [le Planificateur de tâches](automation.md#🪟-windows-task-scheduler) (Windows).

---

Pour plus d’aide, voir les sections [Automatisation](automation.md) et [Paramètres](parameters.md), ou ouvrez un ticket sur [GitHub](https://github.com/geoadmin/service-geocat-harvesting/issues).