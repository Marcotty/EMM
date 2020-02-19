# EMM Console

Description
  Server python permettant la gestion d'appareils mobile utilisant Android Management API
  
Prerequis
  Variable d'environnement
  - GOOGLE_APPLICATION_CREDENTIALS    # pointe vers fichier contenant la clé du compte de service Google
  
  Frameworks Python
  - Flask       # serveur Python
  - requests    # utilisation requêtes HTTP
  - json        # objects json <=> objects python
  - os          # accès variable d'environnement GOOGLE_APPLICATION_CREDENTIALS
  - webbrowser  # ouverture QR_Code d'inscription
  - google.oauth2 import service_account      # Utilisation de comptes de service permettant à l'application d'obtenir les autorisations nécessaire pour accéder à l'API
  - googleapiclient import build              # API cliente Google
  - google_auth_oauthlib.flow import InstalledAppFlow   # Autorisations par défault (?)
  - urllib.parse import urlencode             # permet la création du qr_code
  
  ++++ fichier dépendances
  
Installation
  Télécharger l'archive, extraire dans un dossier, y placer le fichier contenant la clé du compte de service
  Installer Python..
  Dans la console, lancer le serveur >py server.py
  Accès à localhost:5000

Contact 
  fred.marcotty@gmail.com
