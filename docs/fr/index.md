# 🐱 Outil de récolte geocat

> **Automatisez vos envois de métadonnées vers [geocat.ch](https://www.geocat.ch/) en toute simplicité !**

---

## 🌍 Qu'est-ce que le harvesting ?

**Le harvesting** est le processus de collecte et de dépôt automatique de notices de métadonnées (fichiers XML) dans le catalogue geocat.ch.  
Cet outil vous aide à téléverser, mettre à jour et planifier la gestion de vos métadonnées en lot, vous faisant gagner du temps et réduisant les erreurs.

---

## 🚦 Comment utiliser cet outil ? (3 étapes faciles)

### 1️⃣ Installation & Préparation

- Installez Python 3.8+ et les dépendances nécessaires.
- Clonez le dépôt et installez les paquets Python.

[🛠️ Voir la prise en main](getting-started.md)

---

### 2️⃣ Réglez vos paramètres

- Configurez vos identifiants et paramètres API dans `.env` et `config.py`.
- Définissez votre groupe cible, les options de traitement et le dossier contenant vos fichiers XML.

[⚙️ Voir tous les paramètres](parameters.md)

---

### 3️⃣ Automatisez vos envois

- Planifiez l’exécution automatique du script avec **cron** (Linux) ou le **Planificateur de tâches** (Windows).
- Surveillez vos logs pour vérifier le bon déroulement.

[🤖 Guide d’automatisation](automation.md)

---

## 📝 Exemple rapide

```sh
python main.py --path ./metadata --group 42
# Sortie :
# 12 notices de métadonnées envoyées avec succès
```