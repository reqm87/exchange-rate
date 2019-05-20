import datetime

import requests

FIXER_URL = 'http://data.fixer.io/api/latest?access_key=9409a6f3c2f6273668a769f1e97f3444&symbols=USD,MXN'
BANXICO_URL = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/oportuno'


def fixer():
    data = requests.get(FIXER_URL).json()
    value = 100 / data['rates']['USD'] / 100 * data['rates']['MXN']
    last_updated = datetime.datetime.fromtimestamp(
        data['timestamp']
    ).isoformat()
    result = {'fixer': {'value': value, 'last_updated': last_updated}}
    return result


def banxico():
    data = requests.get(
        BANXICO_URL,
        headers={
            'Bmx-Token': '0b85ede92372eda41f7172b12762cd0282621412084dcc6fb9b3c7b06a6ba52b'
        },
    ).json()
    value = float(data['bmx']['series'][0]['datos'][0]['dato'])
    last_updated = datetime.datetime.strptime(
        data['bmx']['series'][0]['datos'][0]['fecha'], '%d/%m/%Y'
    ).isoformat()
    result = {'banxico': {'value': value, 'last_updated': last_updated}}
    return result
