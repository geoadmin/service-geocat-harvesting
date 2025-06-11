# ⚙️ Paramètres de configuration

## 🌱 Variables d’environnement (`.env`)

| Variable            | Obligatoire | Description                  |
|---------------------|-------------|------------------------------|
| `GEOCAT_USERNAME`   | Oui         | Votre identifiant geocat.ch  |
| `GEOCAT_PASSWORD`   | Oui         | Votre mot de passe geocat.ch |

Exemple :
```ini
# .env
GEOCAT_USERNAME=utilisateur@example.com
GEOCAT_PASSWORD=motdepasse
```

---

## 🛠️ Configuration du script (`config.py`)

| Paramètre                   | Obligatoire | Description                                                                                                    | Exemple/Valeur par défaut                             |
|-----------------------------|-------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `API_URL`                   | Oui         | URL de l’API geocat                                                                                           | `"https://www.geocat.ch/geonetwork/srv/api/"`         |
| `PARAMETER_GROUP`           | Oui         | ID du groupe cible (ex. 42 pour Fribourg)                                                                     | `42`                                                  |
| `PARAMETER_UUID_PROCESSING` | Oui         | Que faire en cas de conflit UUID :<br>- `GENERATEUUID` : créer un nouvel UUID<br>- `OVERWRITE` : écraser<br>- `NOTHING` : ignorer | `"OVERWRITE"`                                         |
| `REJECT_IF_INVALID`         | Oui         | Si `True`, accepte les métadonnées invalides ; si `False`, seulement les valides                              | `True`                                                |
| `UPDATE_DATE_STAMP`         | Oui         | Si `True`, met à jour la date après l’envoi                                                                   | `True`                                                |
| `PARAMETER_PUBLISH_TO_ALL`  | Non         | Si `True`, publie pour tous (défaut : `False`)                                                                | `False`                                               |
| `PATH_TO_XML_FILES`         | Oui         | Dossier contenant vos fichiers XML                                                                            | `"./metadata"`                                        |

Exemple :
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

## 🖥️ Options en ligne de commande

Vous pouvez aussi utiliser des options en ligne de commande :

```sh
python main.py --help
```
Exemple de sortie :
```
Usage: main.py [OPTIONS]
Options:
  --path TEXT      Dossier des fichiers XML
  --group INTEGER  ID du groupe cible
  --dry-run        Test sans envoi
```

---

**Astuce :**  
Voir [`config.py`](https://github.com/geoadmin/service-geocat-harvesting/blob/master/config.py) pour plus de détails et les valeurs par défaut.