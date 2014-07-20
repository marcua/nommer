import tweepy
from auth import authenticate
from collections import Counter

"""
This script tells you who the Tweetiest/most prolific people you
follow are.

Fetch the most recent 800 (Twitter limit) tweets on your timeline.
Count how many tweets each person emitted.  Output something like
this:

Period: 2014-07-20 19:00:06 - 2014-07-20 19:31:01 (0:30:55)
Total tweets 8
Tweetiest people (format is "@person - # tweets (% tweets)"):
  person1 - 3 (37.50%)
  person2 - 2 (25.00%)
  person3 - 1 (12.50%)
  person4 - 1 (12.50%)
  person5 - 1 (12.50%)
"""

api = authenticate()

timeline = list(tweepy.Cursor(api.home_timeline, count=200).items(800))
first_date = min(tweet.created_at for tweet in timeline)
last_date = max(tweet.created_at for tweet in timeline)
names = (tweet._json['user']['screen_name'] for tweet in timeline)
name_count = Counter(names)
total_tweets = sum(count for count in name_count.itervalues())
print 'Period: %s - %s (%s)' % (first_date, last_date,
                                last_date - first_date)
print 'Total tweets', total_tweets
print 'Tweetiest people (format is "@person - # tweets (% of total tweets)"):'
for name, count in name_count.most_common(1000):
  print '\t%s - %s (%0.2f%%)' % (name, count,
                                    float(count) / total_tweets * 100)
