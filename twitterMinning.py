import tweepy

def OAuthVeri():
    autho = tweepy.OAuthHandler('-----need to get your own codes-----','-----need to get your own codes-----')
    autho.set_access_token('------need to get your own codes-----','-----need to get your own codes-----')
    api =  tweepy.API(autho)
    return api


def getUserStatistics(user):
    print("Name : ",user.name,'\nUser Screen Name: ',user.screen_name,'\nId: ',user.id, '\ncreated at : ',user.created_at,'\nlocation : ',user.location,'\ndescription : ',user.description,'\nfollowers count: ',user.followers_count,'\nfriends count: ',user.friends_count,'\nfavourites counts : ',user.favourites_count,'\nurl : ',user.url,'\nNo. of posted tweets: ',user.statuses_count)

def getUserFollowers(api):
	print('\nFollowers: ')
	for i in api.followers():
		print(i.name)

def getUserFriends(api):
	print('\nFriends: ')
	for i in api.friends():
		print(i.name)

def getUserTweets(api):
	print('\nTweets: ')
	for tweet in api.user_timeline():
		print(tweet.text)	

class MyStreamListener(tweepy.StreamListener):
	def on_status(self,status):
		print(status.text)

	def on_error(self,status):
		if status==420:
			return False

def main():
    api  =  OAuthVeri()
    print('Application Authorised ')
    #user=api.me()
    listenerOb = MyStreamListener()
    myStream  =  tweepy.Stream(api.auth,listenerOb)
    searchlist = eval(input('Enter search keywords list: '))
    myStream.filter(track = searchlist)
    '''user = api.get_user('@justinbibier')
    getUserStatistics(user)
    getUserFollowers(user)
    getUserFriends(user)
    getUserTweets(user)'''
    print ('Task completed')
    

if __name__ ==  '__main__' :
    main()
    
