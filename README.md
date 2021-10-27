# ansible_deckofcards

Self-made Ansible module for API-lab

In root-folder there is simple Python-script which will use nice API-playground from https://deckofcardsapi.com/

First step is to request new deck of cards
Then it will ask how many random cards you want to pick from deck.

-

Real point here is Ansible module based on that python.
Module is is in library folder and Ansible-playbook is deck.yml.

Ansible is is launched with extra-parameter 'card_count' to give you random cards.

$ ansible-playbook deck.yml -e "card_count=3"
