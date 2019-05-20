import datetime

import requests

FIXER_URL = 'http://data.fixer.io/api/latest?access_key=9409a6f3c2f6273668a769f1e97f3444&symbols=USD,MXN'


def fixer():
    data = requests.get(FIXER_URL).json()
    value = 100 / data['rates']['USD'] / 100 * data['rates']['MXN']
    last_updated = datetime.datetime.fromtimestamp(
        data['timestamp']
    ).isoformat()
    result = {'fixer': {'value': value, 'last_updated': last_updated}}
    return result
