
# Author @balan

import time
from os import name,system

def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# defining driver function
def keyword_sentiment_analyzer(keyword, no_of_tweets):
    '''dockstring
    '''
    
    # importing necessary libraries

    print('\n [INFO] Importing necessery libraries ...')
    
    from tweepy import OAuthHandler,API,Cursor
    from textblob import TextBlob
    import matplotlib.pyplot as plt

    time.sleep(2)

    clear()

    print('\n [INFO] Libraries imported successfully.')

    def percentage(weight_of_item,total_no_item):
        '''dockstringstring
        '''
        return 100*float(weight_of_item)/float(total_no_item)

    print("\n [INFO] Generating Authentications ....")
    
    # access credentials
    api_key = 'your API key'
    api_secret_key = 'your API SECRET key'
    access_token  = 'your ACCESS TOKEN'
    access_token_secret = 'your SECRET ACCESS TOKEN'
    
    # setting up authentication from twitter
    auth = OAuthHandler(api_key,api_secret_key)
    
    # setting up acess tocken
    auth.set_access_token(access_token,access_token_secret)
    
    time.sleep(2)
    
    print("\n [INFO] Authentication credentials generated successfully.")
    
    # setting up API with auth handler
    api = API(auth) 
    
    print("\n [INFO] Searching for relevent tweets ....")
    
    # setting up cursor for tweet search
    tweets = Cursor(api.search, q = keyword).items(no_of_tweets)
    
    time.sleep(2)
    
    print("\n [INFO] Tweets gathered successfully.")
    
    # defining variables
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    
    print("\n [INFO] Calculating polarity ....")
    
    # printing tweets using for loop
    for tweet in tweets:
        #print(tweet.text)
        
        # setting up analyzer token
        analyser = TextBlob(tweet.text)
        
        # finding polarity of tweet from analyzer
        polarity += analyser.sentiment.polarity
        
        # updating the variables based on the polarity
        if analyser.sentiment.polarity == 0:
            neutral += 1
            
        if analyser.sentiment.polarity < 0:
            negative += 1
            
        if analyser.sentiment.polarity > 0:
            positive += 1
    
    time.sleep(2)
    
    print('\n [INFO] Polarity calculated successfully.')
    
    # perentage of positive response
    positive = percentage(positive, no_of_tweets)
    
    #percentage of negative response
    negative = percentage(negative, no_of_tweets)
    
    # percentage of neutral response
    neutral = percentage(neutral, no_of_tweets)
    
    # formatting value to two floating points
    positive = format(positive,'.2f')
    negative = format(negative,'.2f')
    neutral = format(neutral,'.2f')
    
    # display no of tweets and keyword
    print(f"\n {no_of_tweets} people reacting on {keyword} topic .")
    
    time.sleep(2)
    
    # defining list of labels
    labels = ['Positive[' +str(positive) + '%]', 'Negative[' +str(negative) + '%]',
               'Neutral[' +str(neutral) + '%]']
    
    # defining list of sizes of postive, negative and neutral response
    size = [positive, negative, neutral]
    
    # defining list of colors for pie chart
    color = ['grey','black','cyan']
    
    # plotting pie chart
    patches,text = plt.pie(size, colors = color, startangle = 90)
    
    # plotting legend to pie chart
    plt.legend(patches, labels, loc = 'best')
    
    # setting title to the chart
    plt.title(f'Twitter Sentiment Analysis on {keyword} with {no_of_tweets} tweets')
    
    # setting axis at equal
    plt.axis('equal')
    
    print('\n [INFO] Plotting report ...')
    
    time.sleep(3)
    
    # display the plot
    plt.show()

# main function
if __name__ == "__main__":
    
    time.sleep(2)
    
    clear()
    
    # taking keyword input from user
    tag = input('\n\n Enter the topic or hashtag on which you want to analyse Sentiment : ').strip().lower()
    
    # taking number of tweets as input from user
    num = int(input('\n\n Enter the Nmber of tweets on which you want to analyze Sentiment : '))
    
    # call driver function
    keyword_sentiment_analyzer(tag, num)
    
