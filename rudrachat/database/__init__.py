from pymongo import MongoClient

import config

RUDRAdb = MongoClient(config.MONGO_URL)
RUDRA = RUDRAdb["RUDRADb"]["RUDRA"]


from .chats import *
from .users import *
