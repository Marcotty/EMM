import requests
import json
import os
import webbrowser
import urllib.request
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urlencode
# Méthode permettant de créer les crédits d'authentification depuis le compte de service
# Permet de ne pas avoir à autoriser l'application à accéder à l'API à chaque exécution.
def CreationCredits() :
    print('Creation credits autorisations')
    credentials = service_account.Credentials.from_service_account_file(
    filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=['https://www.googleapis.com/auth/androidmanagement'])
    return credentials
    
def Inscription_QR() : 
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)

    print('Authentication succeeded.')
    enterprise_name = 'enterprises/LC0430y1qm'

    policy_name = enterprise_name + '/policies/policy1'

    policy_json = '''
    {
      "applications": [
        {
          "packageName": "com.android.chrome",
          "installType": "KIOSK",
          "defaultPermissionPolicy": "PROMPT"
        }
      ],
      "debuggingFeaturesAllowed": true
    }
    '''
    #Creation politique a partir du json
    androidmanagement.enterprises().policies().patch(
        name=policy_name,
        body=json.loads(policy_json)
    ).execute()
    #Creation du token d'inscription
    enrollment_token = androidmanagement.enterprises().enrollmentTokens().create(
        parent=enterprise_name,
        body={"policyName": policy_name}
    ).execute()

    image = {
        'cht': 'qr',
        'chs': '500x500',
        'chl': enrollment_token['qrCode']
    }

    qrcode_url = 'https://chart.googleapis.com/chart?' + urlencode(image)
    
    print('Please visit this URL to scan the QR code:', qrcode_url)
    print('Ouverture auto')
    #url = urllib.request.urlopen(qrcode_url)
    #print('result code : ' + str(url.getcode()))
    webbrowser.open_new(qrcode_url)
    
    entreprises = androidmanagement.entreprises()
    