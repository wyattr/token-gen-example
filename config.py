import os

LINKEDIN_CLIENT_ID = ('77i6le7rgodc6i')
LINKEDIN_CLIENT_SECRET = ('client_secret')

LINKEDIN_ACCESS_TOKEN_URL = ('https://www.linkedin.com/oauth/v2/accessToken')
LINKEDIN_AUTHORIZE_URL = ('https://www.linkedin.com/oauth/v2/authorization')

LINKEDIN_SCOPE =('rw_conversions,r_ads')


# TODO: update this URI to be the webapp URL and path that will recieve/handle the auth code
#LINKEDIN_REDIRECT_URI_1 = "https://eobrtfs819u9wkj.m.pipedream.net"
LINKEDIN_REDIRECT_URI_1 = "http://127.0.0.1:5000/authcode/"
