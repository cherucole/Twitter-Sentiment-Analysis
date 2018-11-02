from secrets import Oauth_Secrets
import tweepy
from textblob import TextBlob


def getdata(input_hashtag):

    # input_hashtag = 'obama'
    secrets = Oauth_Secrets()
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    N = 100  # number of tweets
    # Tweets = api.user_timeline(id=input_hashtag, count=N)
    Tweets = tweepy.Cursor(api.search, q=input_hashtag, lang="en").items(N)

    negative = 0.0
    positive = 0.0
    negative_count = 0
    neutral_count = 0
    postive_count = 0
    tweets_pos = []
    tweets_neg = []
    tweets_nut = []
    # print(Tweets)
    for tweet in Tweets:
        print(tweet.created_at)
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:
            negative += blob.sentiment.polarity
            negative_count += 1
            tweets_neg.append(tweet.text)
        elif blob.sentiment.polarity == 0:
            neutral_count += 1
            tweets_nut.append(tweet.text)
        else:
            positive += blob.sentiment.polarity
            postive_count += 1
            tweets_pos.append(tweet.text)
    # post = ("Positive ", float(postive_count/N)*100, "%")

    data = {
        'Sample': N,
        'Topic': input_hashtag,
        'Positive': postive_count,
        'Neutral': neutral_count,
        'Negative': negative_count,
        'Nagative_tweets': tweets_neg,
        'Neutral_tweets': tweets_nut,
        'Postive_tweets': tweets_pos
    }
    # print(post)
    print(data)
    return data
    # return [['Sentiment', 'number of tweets'], ['Positive', postive_count],
    #         ['Neutral', neutral_count], ['Negative', negative_count]]
