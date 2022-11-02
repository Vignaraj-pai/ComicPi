from datetime import date, time
from hashlib import md5
from django.shortcuts import render
import requests

# Create your views here.
def index(request) :
    pub_key = "f3841a03f678f45641e27f0155dfa4e7"
    priv_key = "cedf68ccbc6076df412b70be34ac7b61fe4b190f"
    ts = str(time)
    url_hash = md5((ts+priv_key+pub_key).encode()).hexdigest()
    n = 3
    events_url = f"https://gateway.marvel.com:443/v1/public/events?orderBy=-startDate&limit=3&ts={ts}&apikey=f3841a03f678f45641e27f0155dfa4e7&hash={url_hash}"
    comics_url = f"https://gateway.marvel.com:443/v1/public/comics?orderBy=focDate&limit=36&ts={ts}&apikey=f3841a03f678f45641e27f0155dfa4e7&hash={url_hash}"
    current_events = requests.get(events_url).json()
    all_comics = requests.get(comics_url).json()
    comic_list = all_comics["data"]["results"]
    event_list = current_events["data"]["results"]

    event_title = []
    event_desc = []
    event_img = []

    for i in range(len(event_list)) :
        f = event_list[i]
        event_title.append(f['title'])
        event_desc.append(f['description'])
        event_img.append(f['thumbnail']['path'] + '.' + f['thumbnail']['extension'])

    comic_title = []
    comic_url = []
    comic_img = []

    for i in range(len(comic_list)) :
        f = comic_list[i]
        comic_title.append(f['title'])
        comic_url.append(f['urls'][0]['url'])
        comic_img.append(f['thumbnail']['path'] + '.' + f['thumbnail']['extension'])

    
    events = zip(event_title, event_desc, event_img)
    comics = zip(comic_title, comic_url, comic_img)

    context = {'eventlist':events,
                'comiclist':comics 
            } 

    return render(request, "home/index.html", context)
