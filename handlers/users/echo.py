from aiogram import types
import wikipedia
from loader import dp

wikipedia.set_lang("uz")


# Echo bot
@dp.message_handler(state=None)
async def send_weki(message: types.Message):

    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("bu mavzuga oid maqola topilmadi!")
