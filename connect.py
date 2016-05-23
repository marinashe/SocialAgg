import requests
import secrets

URL = "https://graph.facebook.com/oauth/access_token"

r = requests.get(URL, {
    'client_id': secrets.APP_ID,
    'client_secret': secrets.APP_SECRET,
    'grant_type': 'client_credentials',
})

r.raise_for_status()

key, value = r.text.split("=")
assert key == "access_token"

with open("TOKEN.txt", "w") as f:
    f.write(value)

print("OK")