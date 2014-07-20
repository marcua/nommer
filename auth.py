import settings
import tweepy


def authenticate():
  auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
  if not (settings.AUTH_KEY and settings.AUTH_SECRET):
    print ('settings.AUTH_KEY and settings.AUTH_SECRET aren\'t '
           'set, so let\'s get you some')
    redirect_url = auth.get_authorization_url()
    print 'Head to %s and authorize the app' % redirect_url
    verifier = raw_input('Enter your verification code: ').strip()
    token = auth.get_access_token(verifier=verifier)
    print ('To avoid this step in the future, go to settings.py and '
           'set "AUTH_KEY = \'%s\'" and "AUTH_SECRET = \'%s\'"' % 
           (token.key, token.secret))
    settings.AUTH_KEY = token.key
    settings.AUTH_SECRET = token.secret
  auth.set_access_token(settings.AUTH_KEY, settings.AUTH_SECRET)
  return tweepy.API(auth)
