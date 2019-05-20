import datetime

from bs4 import BeautifulSoup


def dof_format(data):
    soup = BeautifulSoup(data, 'html.parser')
    row = soup.find('tr', attrs={'class': 'renglonNon'})
    values = row.text.replace('\n', '').replace('\r', '').split(' ')
    values = list(filter(None, values))
    value = float(values[1])
    last_updated = datetime.datetime.strptime(
        values[0], '%d/%m/%Y'
    ).isoformat()
    result = {'dof': {'value': value, 'last_updated': last_updated}}
    return result


def fixer_format(data):
    value = 100 / data['rates']['USD'] / 100 * data['rates']['MXN']
    last_updated = datetime.datetime.fromtimestamp(
        data['timestamp']
    ).isoformat()
    result = {'fixer': {'value': value, 'last_updated': last_updated}}
    return result


def banxico_format(data):
    value = float(data['bmx']['series'][0]['datos'][0]['dato'])
    last_updated = datetime.datetime.strptime(
        data['bmx']['series'][0]['datos'][0]['fecha'], '%d/%m/%Y'
    ).isoformat()
    result = {'banxico': {'value': value, 'last_updated': last_updated}}
    return result
