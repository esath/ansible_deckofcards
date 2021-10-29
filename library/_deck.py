#!/usr/bin/python

import requests
import json

from ansible.module_utils.basic import AnsibleModule

def run_module():
    
    #Set count variable linked to ansible-playbook
    module_args = dict(
        count=dict(type='str', required=True),
    )
    #Set default results to return when module code exits
    result = dict(
        changed=False,
        original_message='',
        message='',
        my_useful_info={},
    )

    #Enable check-only mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

##### This is start of original Python-code. >>>>

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

    #Set card count and put count-number to request uri
    count = module.params['count']
    urldraw = "https://deckofcardsapi.com/api/deck/"+deckid+"/draw/?count=" + count
    count = int(count)

    #make request for n cards and save result to variable:
    cards = requests.request("GET", urldraw, headers=headers, data=payload)
    cards1 = json.loads(cards.text)
    
#### Original Python-code ends here. Other is for Ansible <<<<<<<<<<<

    #Set JSON-content to result for Ansible output
    result = cards1
    
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
