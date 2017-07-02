import pylab
import  requests
from keys import APP_ACCESS_TOKEN
BASE_URL = 'https://api.instagram.com/v1/'


#function to get user id
def get_user_id(insta_username):

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)

    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'

def get_user_persona(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print "finding and plotting user's interest"
    hash_items={}
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for x in range(0,len(user_media['data'])):
                for y in range(0,len(user_media['data'][x]['tags'])):

                    if user_media['data'][x]['tags'][y] in hash_items:
                        hash_items[user_media['data'][x]['tags'][y]]+=1
                    else:
                        hash_items[user_media['data'][x]['tags'][y]]= 1


        else:
            print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
    print hash_items


get_user_persona('iv_jot')