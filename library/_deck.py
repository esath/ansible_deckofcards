#!/usr/bin/python

import requests
import json

#from ansible.module_utils.basic import *
from ansible.module_utils.basic import AnsibleModule

def run_module():

    module_args = dict(
        count=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
        my_useful_info={},
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

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
    #You need to change integer to string in url!
    #count = input("How many cards you want?")
    count = module.params['count']
    urldraw = "https://deckofcardsapi.com/api/deck/"+deckid+"/draw/?count=" + count
    count = int(count)

    #make request for n cards and save result to variable:
    cards = requests.request("GET", urldraw, headers=headers, data=payload)
    cards1 = json.loads(cards.text)

    result = cards1

    #Make pretty list of cards you got in JSON-format:
#    n=0
#    while n<count:
#            print(cards1["cards"][n]["value"],
#                    cards1["cards"][n]["suit"])
#            n = n + 1

    #module.exit_json(changed=False, meta=response)
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
