# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 23.09.2017

from Virginity.settings import *

SECRET_KEY = os.environ['SECRET_KEY']

# DEBUG = False
# ImGur Client Production

ALLOWED_HOSTS += ['.herokuapp.com']

SITE_ID = 2

IMGUR_CLIENT_ID = '2bcda18a072f658'
IMGUR_CLIENT_SECRET = 'eb16a3a1783ac786362796970602dbf9e59d6768'