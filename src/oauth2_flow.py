# oauth2_flow.py
import configparser
import requests
import urllib.parse
import base64

# Load configuration
config = configparser.ConfigParser()
config.read('../config/config.ini')

client_id = config['TWITTER']['client_id']
redirect_uri = config['TWITTER']['redirect_uri']

# Generate code verifier and code challenge
def generate_code_challenge():
    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).rstrip(b'=').decode('utf-8')
    code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode('utf-8')).digest()).rstrip(b'=').decode('utf-8')
    return code_verifier, code_challenge

code_verifier, code_challenge = generate_code_challenge()

# Build authorization URL
auth_url = (
    f"https://twitter.com/i/oauth2/authorize"
    f"?response_type=code"
    f"&client_id={client_id}"
    f"&redirect_uri={urllib.parse.quote(redirect_uri)}"
    f"&scope=tweet.read tweet.write users.read offline.access"
    f"&state=state"
    f"&code_challenge={code_challenge}"
    f"&code_challenge_method=S256"
)

print(f"Please go to this URL and authorize the app: {auth_url}")

# After authorizing, the user will be redirected to the redirect URI with a code
callback_response = input("Enter the full callback URL: ")

# Extract the authorization code from the callback URL
import re
code = re.search('code=([^&]*)', callback_response).group(1)

# Exchange authorization code for access token
token_url = 'https://api.twitter.com/2/oauth2/token'
data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirect_uri,
    'code_verifier': code_verifier,
    'client_id': client_id
}
response = requests.post(token_url, data=data)
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens['access_token']
    refresh_token = tokens.get('refresh_token')
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)

    # Save the access token to config.ini
    config.set('TWITTER', 'access_token', access_token)
    with open('../config/config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print(f"Error obtaining access token: {response.status_code}")
    print(response.json())
