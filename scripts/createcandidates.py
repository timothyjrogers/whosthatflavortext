import json
import random

with open('AllPrintings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)['data']

scryfall_api = 'https://api.scryfall.com/cards/search'
cards_with_flavortext = {}

sorted_set_codes = list(data.keys())
sorted_set_codes.sort(key=lambda s: data[s]['releaseDate'], reverse=True)

for s in data:
    cards = data[s]['cards']
    for card in cards:
        if 'flavorText' in card:
            name = card['name']
            flavor_text = card['flavorText']
            if name in cards_with_flavortext:
                obj = cards_with_flavortext[name]
                if flavor_text in obj:
                    obj[flavor_text].append(s)
                else:
                    obj[flavor_text] = [s]
                cards_with_flavortext[name] = obj
            else:
                cards_with_flavortext[name] = {}
                cards_with_flavortext[name][flavor_text] = [s]

k = list(cards_with_flavortext.keys())

candidates = []
for k in cards_with_flavortext:
    card = cards_with_flavortext[k]
    for flavor in card:
        candidate = {}
        candidate['name'] = k
        candidate['text'] = flavor
        sets = card[flavor]
        sets.sort(key=lambda x: sorted_set_codes.index(x))
        candidate['sets'] = sets
        candidates.append(candidate)

random.shuffle(candidates)
with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(candidates, f)