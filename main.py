import tweepy
import time
import sys
import json

API_KEY = "0lZtjr49c4SHXbIaFIJJ8QUEx"
API_SECRET_KEY = "u0dqi4dTgy2ReJdI6WDznswmN0ZzHHh9RQQokhZenDkFYIwZYi"
ACCESS_TOKEN = "1395246298371018757-h76If1iEU2froJ0CSLaRI2qZt2iGsP"
ACCESS_TOKEN_SECRET = "a7B3zDuViq0K3mRag2Dm7qashPZgBtf4LgMZKZvEKseGN"


def main():

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    print("##########################################################\n")
    print("Welcome to the Twitter console application.\n")
    print("##########################################################\n\n")

    while(True):
        print("What do you want to do?\n")
        print("Post a tweet -> 0\n")
        print("Check your timeline -> 1\n")
        print("Check the timeline of another user -> 2\n")
        print('Send a DM -> 3\n')
        print('See Global trends -> 4\n')
        print("Exit application -> 5\n")


        option = input('Enter option: ')

        if option == '0':
            text = input('Enter tweet: ')
            try:
                api.update_status(text)
            except Exception as e:
                print(e)
            print("Tweet posted successfully at " + time.asctime())
            print(text)

        elif option == '1':
            tweets = api.home_timeline()

            for tweet in tweets:
                print('\n')
                print(tweet.text)

        elif option == '2':
            user_handle = input('Enter the user handle: ')
            tweets = api.user_timeline(screen_name=user_handle)

            for tweet in tweets:
                print('\n')
                print(tweet.text)

        elif option == '3':
            user_handle = input('Enter the user handle: ')
            user = api.get_user(screen_name=user_handle)
            user_id = user.id_str
            message = input('Enter message: ')
            try:
                api.send_direct_message(user_id, message)
            except Exception as e:
                print(e)

        elif option == '4':
            trends = api.trends_place('1')
            print('\nThese are the current global trends: \n')

            for trend in trends[0]['trends']:
                print(trend['name'] + '\n')

        elif option == '5':
            print('\nThank you for using the Twitter console app...')
            sys.exit()




if __name__ == "__main__":
    main()
