from keys import APP_ACCESS_TOKEN
BASE_URL = 'https://api.instagram.com/v1/'

import pylab,requests

def get_media_by_loc():
    lat=30.7333
    lon=76.7794
    request_url= BASE_URL+'media/search?lat=%f&lng=%f&access_token=%s&distance=5000'%(lat,lon,APP_ACCESS_TOKEN)
    print "finding and plotting trends in chandigarh"
    hash_items = {}
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for x in range(0, len(user_media['data'])):
                for y in range(0, len(user_media['data'][x]['tags'])):

                    # finding user's intrest by counting hash tags
                    if user_media['data'][x]['tags'][y] in hash_items:
                        hash_items[user_media['data'][x]['tags'][y]] += 1
                    else:
                        hash_items[user_media['data'][x]['tags'][y]] = 1


        else:
            print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
    print hash_items

    pylab.figure(1)

    x = range(len(hash_items))
    pylab.xticks(x, hash_items.keys())
    pylab.plot(x, hash_items.values(), "g")

    pylab.show()

get_media_by_loc()