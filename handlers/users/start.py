from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from keyboards.inline.subscription import *
from utils.misc import subscription
from loader import dp, bot
from aiogram.utils.exceptions import TelegramAPIError


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)

        invite_link = await chat.export_invite_link()
        channels_format += f"👉<a> href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Bu Botdan foydalanish uchun, quyidagi kannalrga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)


# @dp.message_handler(commands=['start'])
# async def show_channels(call: types.CallbackQuery):
#     await call.answer(f"Bu Botdan foydalanish uchun, quyidagi kannalrga obuna bo'ling: \n",
#                       reply_markup=channel_button,
#                       disable_web_page_preview=True)


# @dp.callback_query_handler(text="check_subs")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id, channel=channel)
#         channel = await bot.get_chat(channel)
#         if not status:
#             invite_link = await channel.export_invite_link()
#             result += (f"❌<b>{channel.title}</b> kanalga obuna bolmagansiz."
#                        f"<a> href='{invite_link}'>Obuna buling</a>\n\n")
#
#     return await call.message.answer(result, disable_web_page_preview=True)

# await call.message.answer(result, disable_web_page_preview=True)

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅<b>{channel.title}</b> kanalga obuna bolgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌<b>{channel.title}</b> kanalga obuna bolmagansiz."
                       f"<a> href='{invite_link}'>Obuna buling</a>\n\n")
    await call.message.answer(result, disable_web_page_preview=True)
