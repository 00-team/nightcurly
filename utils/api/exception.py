from django.http import JsonResponse


def ErrorResponse(message: str, code: int) -> JsonResponse:
    context = {'error': str(message), 'code': code}
    return JsonResponse(context, status=code)


# default error massage
DEM = 'Error while processing the Request'


class E(Exception):
    '''Custom Error Exception'''
    message = DEM
    code = 400

    def __init__(self, message: str = DEM, code: int = 400):
        self.message = str(message)
        self.code = int(code)

    def __str__(self):
        return self.message

    def __index__(self):
        return self.code

    @property
    def response(self):
        context = {'error': self.message, 'code': self.code}
        return JsonResponse(context, status=self.code)


ACCOUNT_NOT_FOUND = E('Account Not Found', 404)
OWNER_NOT_FOUND = E('Owner Not Found', 404)
VALID_TWITTER = E('this twitter account is not valid')
