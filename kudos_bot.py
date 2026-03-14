import requests
import os
from datetime import datetime, timedelta

CLIENT_ID = os.environ["STRAVA_CLIENT_ID"]
CLIENT_SECRET = os.environ["STRAVA_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["STRAVA_REFRESH_TOKEN"]

# Replace with your friends Strava athlete IDs
FRIEND_IDS = [
    33838225,
    16146822,
    104000316,
    33700832,
    48685070,
    3149069,
    25112217,
    17634020,
    1885506,
    4337921,
    82119700,
    649970,
    68382909,
    20019607,
]

LOOKBACK_HOURS = 2


def get_access_token():
    res = requests.post("https://www.strava.com/oauth/token", data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
    })
    print(res.status_code, res.json())  # add this
    return res.json()["access_token"]


def get_recent_activities(token, athlete_id):
    after = int((datetime.utcnow() - timedelta(hours=LOOKBACK_HOURS)).timestamp())
    res = requests.get(
        "https://www.strava.com/api/v3/athletes/{}/activities".format(athlete_id),
        headers={"Authorization": "Bearer {}".format(token)},
        params={"after": after, "per_page": 10},
    )
    return res.json() if res.status_code == 200 else []


def give_kudo(token, activity_id):
    res = requests.post(
        "https://www.strava.com/api/v3/activities/{}/kudos".format(activity_id),
        headers={"Authorization": "Bearer {}".format(token)},
    )
    return res.status_code == 201


def main():
    token = get_access_token()
    for athlete_id in FRIEND_IDS:
        for activity in get_recent_activities(token, athlete_id):
            aid = activity["id"]
            name = activity.get("name", "unknown")
            status = "Sent" if give_kudo(token, aid) else "Skipped"
            print("{}: {} (ID: {})".format(status, name, aid))


if __name__ == "__main__":
    main()

