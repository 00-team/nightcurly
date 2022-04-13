# path
from pathlib import Path

# django utils
from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible

# files
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

# requests
from requests import get

from mimetypes import guess_extension


@deconstructible
class file_path(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename: str):
        if filename.find('.') == -1:
            ext = ''
        else:
            ext = filename.split('.')[-1]
        name = get_random_string(20)
        return Path(self.path) / f'{name}.{ext}'


def download_file(url: str | None) -> File | None:
    try:
        if not url:
            return

        with get(url, allow_redirects=True, stream=True) as res:

            if res.status_code != 200:
                return

            content_type = res.headers.get('Content-Type')
            ext = guess_extension(content_type)
            temp = NamedTemporaryFile(suffix=ext)

            for chunk in res.iter_content(8192):  # 1024 * 8
                temp.write(chunk)

        return (File(temp), ext, content_type)
    except:
        pass
