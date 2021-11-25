import os
DatabaseURL = os.environ['DATABASE_URL']
ClientID = os.environ['SPOTIFY_CLIENT']
ClientSecret = os.environ['SPOTIFY_SECRET']
RedirectURL = os.environ["SPOTIFY_CALLBACK"]


debug = False
 ## This is for deployed to Heroku, we are not having the debug on in a prod environment, 
 # if it's going to fail its going to fail hidden
SECRET_KEY  = os.environ['SECRET_KEY']
## Refresh when pushed to heroku, for env variablesss