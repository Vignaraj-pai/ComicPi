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
    url = f"https://gateway.marvel.com:443/v1/public/events?orderBy=-startDate&limit=3&ts={ts}&apikey=872b0839cb76a040e58d12840a5cc260&hash={url_hash}"
    
    current_events = requests.get(url).json()

    event_list = current_events["data"]["results"]

    title = []
    desc = []
    img = []

    for i in range(len(event_list)) :
        f = event_list[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['thumbnail']['path'] + '.' + f['thumbnail']['extension'])
    
    mylist = zip(title, desc, img)
    context = {'mylist':mylist}

    return render(request, "home/index.html", context)
