from secrets import Oauth_Secrets
import tweepy
from textblob import TextBlob


def getdata(input_hashtag):

    # input_hashtag = 'obama'
    secrets = Oauth_Secrets()
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    N = 5  # number of tweets
    # Tweets = api.user_timeline(id=input_hashtag, count=N)
    Tweets = tweepy.Cursor(api.search, q=input_hashtag, tweet_mode='extended',
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
    # general_location = []
    # time_negative = {}
    # time_neutral = {}
    # time_positive = {}
    # if len(Tweets) < 1:
    #     print("no tweets for now")
    # else:
    # print(Tweets)
    # the key for profile image on tweet json is 'profile_image_url'
    for tweet in Tweets:
        print(tweet.user.location)  # location works for some
        print(tweet.user.screen_name)  # to show username
        print(tweet.user.profile_image_url)  # to show profile image
        # location works for some
        print('followers are: ' + str(tweet.user.followers_count))  # followers
        # number of user favourites
        print('user favourites are:' + str(tweet.user.favourites_count))
        # number of tweet retweets
        print('retweets are: ' + str(tweet.retweet_count))
        # number of tweet favourites
        print('favs are: ' + str(tweet.favorite_count))
        print(tweet.full_text)  # tweet itself
        # print('retweets are: ' + str(tweet.retweet_count))
        # print('favs are: ' + str(tweet.favorite_count))

        print('string is ' + str(tweet.id_str))  # tweet id
        # print(tweet)
        # print(tweet.text)
        # print(tweet.created_at)
        # print(tweet.user.location)
        # print("placeid:%s" % tweet)
        # print(tweet.id_str, tweet.coordinates, tweet.geo, tweet.geocode)
        # print(tweet.place.country)
        avatar = tweet.user.profile_image_url
        username = tweet.user.screen_name
        followers = tweet.user.followers_count
        retweets = tweet.retweet_count
        likes = tweet.favorite_count
        tweet_id = tweet.id_str
        # general_location.append(tweet.user.location)
        blob = TextBlob(tweet.full_text)
        if blob.sentiment.polarity < 0:
            tweet_full = {}
            negative += blob.sentiment.polarity
            negative_count += 1
            # tweets_neg.append(tweet.text)
            tweet_full['tweet'] = (tweet.full_text)
            tweet_full['username'] = (username)
            tweet_full['avatar'] = (avatar)
            tweet_full['followers'] = (followers)
            tweet_full['retweets'] = (retweets)
            tweet_full['likes'] = (likes)
            tweet_full['tweet_id'] = (tweet_id)

            tweet_id

            tweets_neg.append(tweet_full)
            # time_negative[tweet.created_at] = tweet.text
        elif blob.sentiment.polarity == 0:
            tweet_full = {}

            neutral_count += 1
            # tweets_nut.append(tweet.text)
            tweet_full['tweet'] = (tweet.full_text)
            tweet_full['username'] = (username)
            tweet_full['avatar'] = (avatar)
            tweet_full['followers'] = (followers)
            tweet_full['retweets'] = (retweets)
            tweet_full['likes'] = (likes)
            tweet_full['tweet_id'] = (tweet_id)

            tweets_nut.append(tweet_full)

            # time_neutral[tweet.created_at] = tweet.text
        else:
            positive += blob.sentiment.polarity
            tweet_full = {}

            postive_count += 1
            # tweets_pos.append(tweet.text)
            tweet_full['tweet'] = (tweet.full_text)
            tweet_full['username'] = (username)
            tweet_full['avatar'] = (avatar)
            tweet_full['followers'] = (followers)
            tweet_full['retweets'] = (retweets)
            tweet_full['likes'] = (likes)
            tweet_full['tweet_id'] = (tweet_id)

            tweets_pos.append(tweet_full)
            # time_positive[tweet.created_at] = tweet.text

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
        # 'general_location': general_location,
        # 'time_negative': time_negative,
        # 'time_neutral': time_neutral,
        # 'time_positive': time_positive

    }
    # print(post)
    # print(data)

    return data
    # return [['Sentiment', 'number of tweets'], ['Positive', postive_count],
    #         ['Neutral', neutral_count], ['Negative', negative_count]]
