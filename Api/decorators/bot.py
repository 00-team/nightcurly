from django.http import HttpRequest

# settings
from django.conf import settings

# exceptions
from utils.api.exception import E


def bot_api(view_func):

    def wrap(request: HttpRequest, *args, **kwargs):
        BOT_SECRET = request.headers.get('Authorization')

        if BOT_SECRET == settings.SECRETS.BOT_SECRET:
            return view_func(request, *args, **kwargs)

        return E('Unauthorized', 401).response

    return wrap
