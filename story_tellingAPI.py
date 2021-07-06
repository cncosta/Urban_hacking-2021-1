import requests
import random as rd

inicio = 'Is The year 2050 an art made by '
opcion0 = ['humans ', 'artificial inteligence']
opcion1 = ['Has beccame very popular. ', 'has disappeared. ','has been frobidden. ']

text = str.encode(inicio+rd.choice(opcion0)+rd.choice(opcion1))

r = requests.post(
    "https://api.deepai.org/api/text-generator",
    files={
        'text': text,
    },
    headers={'api-key': 'bb45c840-2ea1-4184-94a6-b903960fd59f'}
)
print(r.json()['output'])
