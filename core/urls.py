from settings import FIXER_API_ACCESS_KEY

DOF_URL = 'http://www.banxico.org.mx/tipcamb/tipCamMIAction.do'
FIXER_URL = 'http://data.fixer.io/api/latest?access_key={}&symbols=USD,MXN'.format(
    FIXER_API_ACCESS_KEY
)
BANXICO_URL = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/oportuno'
