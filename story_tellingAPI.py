import requests
from parametros import KEY #key personal


def story_telling(enunciado):
    text = str.encode(enunciado)
    r = requests.post(
    "https://api.deepai.org/api/text-generator",
    files={
        'text': text,
    },
    headers={'api-key':  KEY} #llave personal
    )
    return r.json()['output']


if __name__ == '__main__':
    import random as rd
    
    inicio = 'Is The year 2050 an art made by '
    opcion0 = ['humans ', 'artificial inteligence']
    opcion1 = ['Has beccame very popular. ', 'has disappeared. ','has been frobidden. ']
    
    frase  = inicio+rd.choice(opcion0)+rd.choice(opcion1)
    print(story_telling(frase))
