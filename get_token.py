import requests

CLIENT_ID = "211850"
CLIENT_SECRET = "ee74c2d6852014c4e6f658a9bce4e2c963be83b8"

url = (
    "https://www.strava.com/oauth/authorize"
    "?client_id={}"
    "&response_type=code"
    "&redirect_uri=http://localhost"
    "&approval_prompt=force"
    "&scope=activity:read_all,activity:write"
).format(CLIENT_ID)

print("Open this URL in your browser:")
print(url)
code = input("Paste the code from the redirect URL: ")

res = requests.post("https://www.strava.com/oauth/token", data={
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": code,
    "grant_type": "authorization_code",
})
print("Refresh token:", res.json()["refresh_token"])
