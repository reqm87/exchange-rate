import requests
from serializer import banxico_format, dof_format, fixer_format
from settings import BANXICO_API_TOKEN
from urls import BANXICO_URL, DOF_URL, FIXER_URL


def dof():
    response = requests.get(DOF_URL)
    return dof_format(response.text)


def fixer():
    response = requests.get(FIXER_URL)
    return fixer_format(response.json())


def banxico():
    response = requests.get(
        BANXICO_URL, headers={'Bmx-Token': BANXICO_API_TOKEN}
    )
    return banxico_format(response.json())
