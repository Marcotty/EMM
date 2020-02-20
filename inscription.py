import requests
import json
import os
import webbrowser
import urllib.request
from google.oauth2 import service_account
from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urlencode

def test() :
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
    print('Authentication succeeded.')
    enterprise_name = 'enterprises/LC0430y1qm'
    entreprises = androidmanagement.enterprises().get(name = enterprise_name).execute()
    names = entreprises['name']
    print('Entreprise name : ' + names)
    
    response = androidmanagement.enterprises().devices().list(parent = enterprise_name).execute()
    txt = json.dumps(response, indent=4)
    print(txt)
    devices = response['devices']
    for device in devices:
        print('Name: ' + device['name'])
        
#Méthode permettant de supprimer TOUS les devices (développement)
def DeleteAllDevices():
    print('Suppression de tous les devices')
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
    if androidmanagement:
        print('Authentication succeeded.')
    devices = ListDevices()
    for device in devices:
        print('Suppression de ' + device['name'])
        androidmanagement.enterprises().devices().delete(name = device['name'])
        
#Méthode permettant de supprimer un device grâce à son nom
def DeleteDevices(NomDevice):
    print('Suppression du device ' + NomDevice)
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
    if androidmanagement:
        print('Authentication succeeded.')
    response = androidmanagement.enterprises().devices().delete(name = NomDevice).execute()
    if response == 200:
        print('Suppression ok')
    elif response == 404:
        print('Pas de device portant ce nom : ' + NomDevice)
    else:
        #print(response.to_json())
        print('erreur?')

#Méthode permettant de convertir un objet python en objet json
def ObjetToJson(objet):
    device_json = json.dumps(objet, indent=4)
    return device_json
#Méthode permettant de retourner la liste des devices
def ListDevices():
    print('Retourne la liste des devices')
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
    if androidmanagement:
        print('Authentication succeeded.')
    enterprise_name = 'enterprises/LC0430y1qm'    
    response = androidmanagement.enterprises().devices().list(parent = enterprise_name).execute()
    devices = response['devices']
    return devices
#Méthode qui permet d'afficher dans la console la liste des devices appartenant à l'organisation
def AffListDevices() :
    print('Affichage des devices')
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
    if androidmanagement:
        print('Authentication succeeded.')
    enterprise_name = 'enterprises/LC0430y1qm'    
    response = androidmanagement.enterprises().devices().list(parent = enterprise_name).execute()
    if response:
        devices = response['devices']
        i=0
        for device in devices:
            i+=1
            print('\nDevice n°{} :'.format(i))
            print('Name: ' + device['name'])
            print('Politique: ' + device['policyName'])
            print('UserName: ' + device['userName'])
            print('ManagementMode: ' + device['managementMode'])
            print('Date inscription: ' + device['enrollmentTime'])
            if 'softwareInfo' in device:
                softwareInfo = device['softwareInfo']
                #print('Marque: ' + softwareInfo['brand'])
                print('Version Android: ' + softwareInfo['androidVersion'])
                print('Langage Systeme: ' + softwareInfo['primaryLanguageCode'])
            if 'hardwareInfo' in device:
                hardwareInfo = device['hardwareInfo']
                print('Marque: ' + hardwareInfo['brand'])
                print('Modèle: ' + hardwareInfo['model']) 
            # Afficher l'objet en JSON
            #print(ObjetToJson(device))
    else:
        print('Aucun device trouvé')
def AffListPolicies() :
    print('Affichage des politiques')
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
    if androidmanagement:
        print('Authentication succeeded.')
    enterprise_name = 'enterprises/LC0430y1qm'    
    response = androidmanagement.enterprises().policies().list(parent = enterprise_name).execute()
    policies = response['policies']
    i=0
    for policy in policies:
        i+=1
        print('\Politique n°{} :'.format(i))
        print(ObjetToJson(policy))
        
# Méthode permettant de créer les crédits d'authentification depuis le compte de service
# Permet de ne pas avoir à autoriser l'application à accéder à l'API à chaque exécution.
def CreationCredits() :
    print('Creation credits autorisations')
    credentials = service_account.Credentials.from_service_account_file(
    filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=['https://www.googleapis.com/auth/androidmanagement'])
    return credentials
    
def InscriptionQR(NomPolitique):
    # Paste your project ID here.
    cloud_project_id = 'projettest-268014'
    
    #Create credentials
    credentials = CreationCredits()
    # Create the API client.
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)

    print('Authentication succeeded.')
    enterprise_name = 'enterprises/LC0430y1qm'
    
    #Creation du token d'inscription
    enrollment_token = androidmanagement.enterprises().enrollmentTokens().create(
        parent=enterprise_name,
        body={"policyName": NomPolitique}
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
    
#Méthode permettant d'inscrire les devices en utilisant un qr code
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
      "kioskCustomization": {
          "powerButtonActions" : "POWER_BUTTON_BLOCKED"
        },
      "debuggingFeaturesAllowed": true,
      "adjustVolumeDisabled": true
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