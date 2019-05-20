BANXICO_API_TOKEN = 'api-token'
FIXER_API_ACCESS_KEY = 'api-access-key'


try:
    from config.local_settings import *
except ImportError:
    pass
