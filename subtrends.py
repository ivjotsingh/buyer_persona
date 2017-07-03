import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pylab
import requests
from keys import APP_ACCESS_TOKEN
BASE_URL = 'https://api.instagram.com/v1/'

def get_media_by_tag(tag):
    request_url=BASE_URL+ 'tags/%s/media/recent?access_token=%s'%(tag,APP_ACCESS_TOKEN)

    print "finding and plotting subtrends"
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
    hash_items.pop(tag)
    print hash_items

    pylab.figure(1)

    x = range(len(hash_items))
    pylab.xticks(x, hash_items.keys())
    pylab.plot(x, hash_items.values(), "g")

    pylab.show()

    wordcloud = WordCloud().generate_from_frequencies(hash_items)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


trend=raw_input("which trend to be searched")
get_media_by_tag(trend)