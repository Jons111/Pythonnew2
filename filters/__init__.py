from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . guruhlar_uchun import Guruh
from .kanallar_uchun import Kanal
from .Userlar_uchun import Shaxsiy

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(Guruh)
    dp.filters_factory.bind(Shaxsiy)
    dp.filters_factory.bind(Kanal)
