# 🤖 Automatisation

Automatisez vos envois de métadonnées pour ne jamais oublier un lot !

---

## 🐧 Linux (cron)

Planifiez l’exécution automatique du script avec `cron`.

1. Éditez votre crontab :
    ```sh
    crontab -e
    ```
2. Ajoutez une ligne pour exécuter le script chaque heure (adaptez le chemin !) :
    ```sh
    0 * * * * /usr/bin/python3 /chemin/vers/main.py >> /var/log/geocat.log 2>&1
    ```
    - `0 * * * *` = chaque heure pile
    - Modifiez `/usr/bin/python3` et `/chemin/vers/main.py` selon votre installation

3. Redémarrez cron si besoin :
    ```sh
    sudo service cron restart
    ```

---

## 🪟 Windows (Planificateur de tâches)

Automatisez le script sous Windows avec le Planificateur de tâches :

1. Ouvrez le **Planificateur de tâches** depuis le menu Démarrer.
2. Créez une **tâche de base**.
3. Définissez le **déclencheur** (ex. quotidien, horaire).
4. Pour **Action**, choisissez "Démarrer un programme" :
    - **Programme/script** : `python.exe`
    - **Ajouter des arguments** : `C:\chemin\vers\main.py`
    - **Démarrer dans** : `C:\chemin\vers\votre\projet` (optionnel mais recommandé)
5. Terminez et activez la tâche.

> 💡 Si vous utilisez un environnement virtuel, indiquez le chemin vers `venv\Scripts\python.exe`.

---

## 📈 Suivi & logs

| Fichier log               | Utilité                      |
|---------------------------|------------------------------|
| `/var/log/geocat.log`     | Toutes les sorties et erreurs|
| `errors.log`              | Erreurs critiques seulement  |

Surveillez les logs en temps réel (Linux) :
```sh
tail -f /var/log/geocat.log
```

Exemple de sortie :
```
[INFO] 2023-06-01 10:00: - Traitement de 3 nouveaux fichiers
```

---

!!! tip "Astuce"
    Testez votre automatisation d’abord avec un dry run :
    ```sh
    python main.py --dry-run
    ```

---

**Besoin d’aide ?**  
Consultez les sections [Prise en main](getting-started.md) et [Paramètres](parameters.md), ou ouvrez un ticket sur [GitHub](https://github.com/geoadmin/service-geocat-harvesting/issues).