# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App

# Using PythonAnywhere here are some settings:

# Application name: ChuckList PythonAnywhere
# Homepage Url: https://drchuck.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://drchuck.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = '12928173ff1519103d33'
SOCIAL_AUTH_GITHUB_SECRET = '0fb304228b004f321a4bf0bdb18462625026d1fb'

# Ask for the user's email (don't edit this line)
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

# Note you may not get email for github users that don't make their
# email public - that is OK

# For detail: https://readthedocs.org/projects/python-social-auth/downloads/pdf/latest/

# Using ngrok is hard because the url changes every time you start ngrok

# # If you are running on localhost, here are some settings:
#
# Application name: Mysite Local
# Homepage Url: http://localhost:8000
# Application Description: mysite app
# Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github/