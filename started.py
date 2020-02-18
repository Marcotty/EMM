import requests
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urlencode

# Paste your project ID here.
cloud_project_id = 'projettest-268014'

# This is a public OAuth config, you can use it to run this guide but please use
# different credentials when building your own solution. 
CLIENT_CONFIG = {
    'installed': {
        'client_id':'882252295571-uvkkfelq073vq73bbq9cmr0rn8bt80ee.apps.googleusercontent.com',
        'client_secret': 'S2QcoBe0jxNLUoqnpeksCLxI',
        'auth_uri':'https://accounts.google.com/o/oauth2/auth',
        'token_uri':'https://accounts.google.com/o/oauth2/token'
    }
}
SCOPES = ['https://www.googleapis.com/auth/androidmanagement']

# Run the OAuth flow.
flow = InstalledAppFlow.from_client_config(CLIENT_CONFIG, SCOPES)
credentials = flow.run_console()

# Create the API client.
androidmanagement = build('androidmanagement', 'v1', credentials=credentials)

print('\nAuthentication succeeded.')
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

#response = requests.get('https://androidmanagement.googleapis.com/v1/{name=enterprises/LC0430y1qm}')
#print(response)
#print('tests reponse REST :')
#print(reponse.status_code)

#GET https://androidmanagement.googleapis.com/v1/{name=enterprises/*}