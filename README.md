# Strava Auto Kudos Bot

Sends kudos to a list of Strava friends every 2 hours via GitHub Actions.

## Setup

1. Create a Strava API app at https://www.strava.com/settings/api
   - Callback domain: localhost

2. Run get_token.py locally to get your refresh token
   - Fill in your Client ID and Secret
   - Run: python get_token.py
   - Copy the refresh token printed at the end

3. Edit FRIEND_IDS in kudos_bot.py
   - Find athlete IDs in the URL of a friend's Strava profile

4. Push this folder to a new GitHub repo

5. Add secrets in GitHub: Settings > Secrets and variables > Actions
   - STRAVA_CLIENT_ID
   - STRAVA_CLIENT_SECRET
   - STRAVA_REFRESH_TOKEN

6. Go to Actions tab and run the workflow manually to test
