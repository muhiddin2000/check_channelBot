from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs")
    ]]
)
# channel_button = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Test_1",callback_data="channels", url='https://t.me/+D4TUD7eDlCpiZTIy'),
#             InlineKeyboardButton(text="Test_2",callback_data="channels", url='https://t.me/test_2chan'),
#
#         ],
#         [
#             InlineKeyboardButton(text="Test_3",callback_data="channels", url='https://t.me/tesss_3'),
#             InlineKeyboardButton(text="Test_4",callback_data="channels", url='https://t.me/+7CVWwbxbpPszYjky'),
#
#         ],
#         [
#             InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs")
#         ],
#     ]
#
# )
