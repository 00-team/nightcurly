# conf
from django.conf import settings


SECRETS = settings.SECRETS

HOST = 'https://' + SECRETS.EXTERNAL_HOST


DEFAULT_USERNAME = 'Nightcurly'
DEFAULT_AVATAR = 'https://cdn.discordapp.com/attachments/731174051170746500/814603567704047646/00_logo_f27.png'

ACCOUNT = SECRETS.WEBHOOKS['ACCOUNT']
BOT_USER = SECRETS.WEBHOOKS['BOT_USER']
DEBUG_HOOK = SECRETS.WEBHOOKS['DEBUG']

HR = '\n' + ('-' * 50) + '\n'

ACCOUNT_STATUS = {
    'new': (1494431, 'New Account'),
    'update': (3526771, 'Edit Account'),
    'delete': (14811960, 'Delete Account'),
}

TWITTER_STATUS = {
    'connect': (3526771, 'Twitter Connected'),
    'reconnect': (1494431, 'Twitter Reconnected'),
    'disconnect': (14811960, 'Twitter Disconnected'),
}
