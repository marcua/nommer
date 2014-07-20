A collection of tools to nom on the tweet stream:
  * `timeline_stats.py` will tell you who the most prolific/tweetiest people you follow are.
  * that's it for now.  Yay Sunday afternoons!

## Installation
At the command line, type the following:

```bash
git clone git@github.com:marcua/nommer.git
cd nommer
pip install -r requirements.txt
cp settings.py.template settings.py
```

## Authenticating your account

  * [Create a new Twitter app](https://apps.twitter.com/app/new).
  * Copy its key/secret to `API_KEY`/`API_SECRET` in the `settings.py` file.
  * Run a script, like `python timeline_stats.py`
  * The script will provide you with a URL to visit.
  * Go to the URL and permit your application to access your account.
  * Copy the verifier token to the waiting script.
  * Copy the `AUTH_KEY`/`AUTH_SECRET` into `settings.py`.
  * Profit.

## Contributing

Issue a pull request.  I'm friendly