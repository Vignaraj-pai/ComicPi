from datetime import date, time
from hashlib import md5
from django.shortcuts import render
import requests

# Create your views here.
def index(request) :
    pub_key = "872b0839cb76a040e58d12840a5cc260"
    priv_key = "abf619c0eb0d1a5db9b5c29e85ae0589d8ffff0a"
    ts = str(time)
    url_hash = md5((ts+priv_key+pub_key).encode()).hexdigest()
    n = 3
    events_url = f"https://gateway.marvel.com:443/v1/public/events?orderBy=-startDate&limit=3&ts={ts}&apikey=872b0839cb76a040e58d12840a5cc260&hash={url_hash}"
    comics_url = f"https://gateway.marvel.com:443/v1/public/comics?orderBy=focDate&limit=16&ts={ts}&apikey=872b0839cb76a040e58d12840a5cc260&hash={url_hash}"
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
    comic_issue = []
    comic_img = []

    for i in range(len(comic_list)) :
        f = comic_list[i]
        comic_title.append(f['title'])
        comic_issue.append(f['issueNumber'])
        comic_img.append(f['thumbnail']['path'] + '.' + f['thumbnail']['extension'])

    
    events = zip(event_title, event_desc, event_img)
    comics = zip(comic_title, comic_issue, comic_img)

    context = {'eventlist':events,
                'comiclist':comics 
            } 

    return render(request, "home/index.html", context)
