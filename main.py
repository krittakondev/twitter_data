import snscrape.modules.twitter as sntwitter
import pandas as pd
import time


query = "#ขายรหัส"
tweets = []
# tweets = []
limit = 5000
delay = 60 #sec
out_path = "./data/tweets.csv"



try:
    data = pd.read_csv(out_path)
    for tw in data.to_numpy():
        tweets.append(tw)
        # print(type(tw[1]))
except FileNotFoundError:
    print('not found tweets.csv')
    tweets = []
    
    
# print(tweets)
while True:
    
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        # url_tweet = tweet
        # tweet = vars(tweet)
        # print(tweet)
        # print(len(tweets))
        # break
        if len(tweets) == limit:
            break
        else:
            for i in range(len(tweets)):
                # print(tweets[i][0], tweet.date)
                if(tweets[i][1] == tweet.username and tweets[i][2] == tweet.content):
                    print("skip eiei\n\n")
                    break
                else:
                    if(len(tweets) == i+1):
                        print("append")
                        print(tweet)
                        try:
                            tweets.append([tweet.date, tweet.username, tweet.content])
                        except:
                            pass

            if(len(tweets)==0):
                print("append")
                print(tweet)
                tweets.append([tweet.date, tweet.username, tweet.content])

            df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
            print("save file!!!", end="\n")
            df.to_csv(out_path, index=False)
        
    
    print("delay: ", delay)
    time.sleep(delay)
# to save to csv