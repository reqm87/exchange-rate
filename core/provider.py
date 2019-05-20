import datetime

import requests
from bs4 import BeautifulSoup
from settings import BANXICO_API_TOKEN
from urls import BANXICO_URL, DOF_URL, FIXER_URL


def dof():
    response = requests.get(DOF_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    row = soup.find('tr', attrs={'class': 'renglonNon'})
    values = row.text.replace('\n', '').replace('\r', '').split(' ')
    values = list(filter(None, values))
    value = float(values[1])
    last_updated = datetime.datetime.strptime(
        values[0], '%d/%m/%Y'
    ).isoformat()
    result = {'dof': {'value': value, 'last_updated': last_updated}}
    return result


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
        BANXICO_URL, headers={'Bmx-Token': BANXICO_API_TOKEN}
    ).json()
    value = float(data['bmx']['series'][0]['datos'][0]['dato'])
    last_updated = datetime.datetime.strptime(
        data['bmx']['series'][0]['datos'][0]['fecha'], '%d/%m/%Y'
    ).isoformat()
    result = {'banxico': {'value': value, 'last_updated': last_updated}}
    return result
