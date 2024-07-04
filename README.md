### 🏠 Tapo P110 Energy Monitoring

**Introduction**
Ce projet de recherche consiste à suivre la consommation énergétique de trois robots en temps réel et à créer un tableau de bord de visualisation. L'objectif est de surveiller l'efficacité énergétique et de prévenir les surcharges en éteignant automatiquement les prises intelligentes lorsque la consommation dépasse un seuil spécifié.

**Fonctionnalités**

**📊 Surveillance en temps réel** : Suivi continu de la consommation électrique des robots via les prises intelligentes TP-Link Tapo P110.
**🚦 Extinction automatique** : Lorsque la consommation dépasse un seuil spécifié, la prise intelligente s'éteint automatiquement pour prévenir les surcharges.

**Prérequis**
Python 3.x
Bibliothèques Python nécessaires (à installer via pip):
   ```bash
requests
json
Installation
Clonez ce dépôt et installez les dépendances nécessaires :
   ```
bash
Copy code
   ```bash
git clone https://github.com/votre-utilisateur/Tapo-P110-Energy-monitoring.git
cd Tapo-P110-Energy-monitoring
pip install -r requirements.txt
   ```
Utilisation
Ouvrez le fichier p110monitor.py.
Configurez les variables suivantes :
python
Copy code
   ```bash
device_ip = '172.20.10.9'  # Remplacez par l'adresse IP de votre TP-Link Tapo P110
threshold = 2000  # Remplacez par le seuil de puissance en watts
   ```
Lancez le script :

   ```bash
python p110monitor.py
Configuration
Modifiez les variables dans le script pour adapter la surveillance à votre configuration :
   ```

**device_ip**: L'adresse IP de votre TP-Link Tapo P110.

**threshold**: Le seuil de consommation en watts au-delà duquel la prise intelligente sera éteinte.

## Tableau de Bord

Un tableau de bord de visualisation des données de consommation énergétique sera développé pour fournir une interface utilisateur intuitive pour l'analyse des données. Ce tableau de bord permettra de :

Visualiser les données de consommation en temps réel.

Analyser les tendances de consommation sur différentes périodes.



   Pour plus d'informations, Consultez le rapport ci-dessous : Dashboard Consommation 3 convoyeurs.pbix


### 📄 Rapport de Projet

Contributions
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.



