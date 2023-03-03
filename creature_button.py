from aiogram import types
from bot_data import BotData
from aiogram.dispatcher.filters.state import State, StatesGroup

bd = BotData()


class CreatureButton():
    async def create_button(self, message, name_button='', text_message='', state='*'):
        keyboard = types.InlineKeyboardMarkup(one_time_keyboard=True)
        if text_message == "Нажмите кнопку, чтобы начать опрос":
            keyboard.add(types.InlineKeyboardButton(text=name_button, callback_data="name_servey"))
        elif text_message == "Нажмите кнопку, чтобы продолжить опрос":
            keyboard.add(types.InlineKeyboardButton(text=name_button, callback_data="continue_servey"))
        else:
            keyboard.add(types.InlineKeyboardButton(text=name_button, callback_data="home"))
        await message.answer(text_message, reply_markup=keyboard)
