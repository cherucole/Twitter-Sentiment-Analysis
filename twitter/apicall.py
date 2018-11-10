from secrets import Oauth_Secrets
import tweepy
from textblob import TextBlob


def getdata(input_hashtag):

    # input_hashtag = 'obama'
    secrets = Oauth_Secrets()
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    N = 1  # number of tweets
    # Tweets = api.user_timeline(id=input_hashtag, count=N)
    Tweets = tweepy.Cursor(api.search, q=input_hashtag,
                           lang="en").items(N)
    # Tweets = api.geo_search(query='Kenya', granularity="country")
    # print(Tweets.text[0])
    negative = 0.0
    positive = 0.0
    negative_count = 0
    neutral_count = 0
    postive_count = 0
    tweets_pos = []
    tweets_neg = []
    tweets_nut = []
    general_location = []
    time_negative = {}
    time_neutral = {}
    time_positive = {}
    # if len(Tweets) < 1:
    #     print("no tweets for now")
    # else:
    # print(Tweets)
    # the key for profile image on tweet json is 'profile_image_url'
    for tweet in Tweets:
        print(tweet.user.location)  # location works for some
        print(tweet.user.screen_name)  # location works for some
        print(tweet.user.profile_image_url)  # location works for some
        # location works for some
        print('followers are: ' + str(tweet.user.followers_count))
        print('user favourites are:' + str(tweet.user.favourites_count))
        print('retweets are: ' + str(tweet.retweet_count))
        print('favs are: ' + str(tweet.favorite_count))
        print(tweet.text)
        # print('retweets are: ' + str(tweet.retweet_count))
        # print('favs are: ' + str(tweet.favorite_count))

        print('string is ' + str(tweet.id_str))
        # print(tweet)
        # print(tweet.text)
        # print(tweet.created_at)
        # print(tweet.user.location)
        # print("placeid:%s" % tweet)
        # print(tweet.id_str, tweet.coordinates, tweet.geo, tweet.geocode)
        # print(tweet.place.country)
        general_location.append(tweet.user.location)
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:
            negative += blob.sentiment.polarity
            negative_count += 1
            tweets_neg.append(tweet.text)
            time_negative[tweet.created_at] = tweet.text
        elif blob.sentiment.polarity == 0:
            neutral_count += 1
            tweets_nut.append(tweet.text)
            time_neutral[tweet.created_at] = tweet.text
        else:
            positive += blob.sentiment.polarity
            postive_count += 1
            tweets_pos.append(tweet.text)
            time_positive[tweet.created_at] = tweet.text

    # post = ("Positive ", float(postive_count/N)*100, "%")

    data = {
        'Sample': N,
        'Topic': input_hashtag,
        'Positive': postive_count,
        'Neutral': neutral_count,
        'Negative': negative_count,
        'Negative_tweets': tweets_neg,
        'Neutral_tweets': tweets_nut,
        'Postive_tweets': tweets_pos,
        'general_location': general_location,
        'time_negative': time_negative,
        'time_neutral': time_neutral,
        'time_positive': time_positive

    }
    # print(post)
    # print(data)

    return data
    # return [['Sentiment', 'number of tweets'], ['Positive', postive_count],
    #         ['Neutral', neutral_count], ['Negative', negative_count]]
