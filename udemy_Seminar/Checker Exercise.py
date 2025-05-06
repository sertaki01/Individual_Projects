tweet = input("Enter your tweet: ")

tweet_length = len(tweet)

max_tweet = 140

long_tweet = tweet_length - max_tweet

if tweet_length < 140:
    print(f"That {tweet_length} char tweet will work!")
else:
    print(f"Your {tweet_length} char tweet is {long_tweet} chars too long")

