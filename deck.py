import requests
import json

#Set default content for REST
payload={}
headers = {}

#Get new deck of cards
url = "https://deckofcardsapi.com/api/deck/new/"
response = requests.request("GET", url, headers=headers, data=payload)
responsedict = json.loads(response.text)
deckid = responsedict["deck_id"]

#Shuffle your new deck
urlshuffle = "https://deckofcardsapi.com/api/deck/"+deckid+"/shuffle/"
shuffle = requests.request("GET", urlshuffle, headers=headers, data=payload)

#Ask how many cards you want and put count-number to request uri
count = input("How many cards you want?")
urldraw = "https://deckofcardsapi.com/api/deck/"+deckid+"/draw/?count=" + count
count = int(count)

#make request for n cards and save result to variable:
cards = requests.request("GET", urldraw, headers=headers, data=payload)
cards1 = json.loads(cards.text)

#Make pretty list of cards you got in JSON-format:
n=0
while n<count:
        print(cards1["cards"][n]["value"],
              cards1["cards"][n]["suit"])
        n = n + 1
