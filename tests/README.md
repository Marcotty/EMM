 # EMM Console

Description
## Description
  Server python permettant la gestion d'appareils mobile utilisant Android Management API
  
Prerequis
## Prerequis
  Variable d'environnement
  - GOOGLE_APPLICATION_CREDENTIALS    # pointe vers fichier contenant la clé du compte de service Google
  
  Frameworks Python
  ### Packages Python
  - Flask       # serveur Python
  - requests    # utilisation requêtes HTTP
  - json        # objects json <=> objects python
@ -18,13 +18,16 @@ Prerequis
  - google_auth_oauthlib.flow import InstalledAppFlow   # Autorisations par défault (?)
  - urllib.parse import urlencode             # permet la création du qr_code
  
  + fichier dépendances => importer les dépendances => py -m pip install -r requirements.txt
  
Installation
  + fichier dépendances => importer les dépendances => 
  ```bash
  py -m pip install -r requirements.txt
  ```
 
## Installation
  Télécharger l'archive, extraire dans un dossier, y placer le fichier contenant la clé du compte de service
  Installer Python..
  Dans la console, lancer le serveur >py server.py
  Accès à localhost:5000

Contact 
## Contact 
  fred.marcotty@gmail.com