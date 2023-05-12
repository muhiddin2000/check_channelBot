from typing import Union
from aiogram import Bot


async def check(user_id, channel: Union[int, str]):
    bot = Bot.get_current()
    membor = await bot.get_chat_member(user_id=user_id, chat_id=channel)
    return membor.is_chat_member()
