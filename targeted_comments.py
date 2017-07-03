
import requests
from keys import APP_ACCESS_TOKEN
BASE_URL = 'https://api.instagram.com/v1/'

def get_media_by_tag(tag):
    request_url=BASE_URL+ 'tags/%s/media/recent?access_token=%s'%(tag,APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for x in range(0,len(user_media['data'])):
                post_a_comment(user_media['data'][x]['id'])


        else:
            print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
    return None


def post_a_comment(media_id):

    comment_text = "Nice"
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = BASE_URL + 'media/%s/comments' % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

get_media_by_tag("chandigarh")