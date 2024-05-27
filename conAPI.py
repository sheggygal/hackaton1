import requests
import base64
from urllib import parse
import webbrowser
from requests_oauthlib import OAuth2Session

# Your Spotify app credentials
client_id = 'c2323a3276464f3b98085f8da3723fce'
client_secret = '6dbe41aa27574c28864599c460ce2c22'
redirect_uri = 'http://localhost:8888/callback'  # This should match the Redirect URI you set in your Spotify app

# OAuth2 Endpoints
auth_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'

# Step 1: Authorization Request
scope = 'user-read-private user-read-email'
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url(auth_url)

# Open the authorization URL in the browser
webbrowser.open(authorization_url)

# Step 2: User authorization and redirect
# The user will authorize the app and be redirected to the callback URL with a code
# You need to manually copy the code from the URL and paste it below

authorization_response = input('Enter the full callback URL: ')

# Step 3: Token Request
token = oauth.fetch_token(token_url, authorization_response=authorization_response,
                          client_secret=client_secret)

# Access token
access_token = token['access_token']

# Now you can use the access token to make authorized requests to the Spotify API
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Example: Get user profile
response = requests.get('https://api.spotify.com/v1/me', headers=headers)
print(response.json())

