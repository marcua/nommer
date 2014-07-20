import tweepy
from auth import authenticate
from collections import Counter

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
print 'Tweetiest people:'
for name, count in name_count.most_common(1000):
  print '\t%s - %s (%0.2f%%)' % (name, count,
                                    float(count) / total_tweets * 100)
