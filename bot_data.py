from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class BotData():
    def __init__(self):
        self.TOKEN = "6138231355:AAGM9k41FIUbRoU4pBvqmGr0qB8nFbHZv2o"
        self.storage = MemoryStorage()
        self.bot = Bot(token=self.TOKEN)
        self.dp = Dispatcher(bot=self.bot, storage=self.storage)
        self.count_answer: int = 1
        self.answers = {}
        self.questions = {
            1: "1.Как вас зовут?",
            2: "2.Какая ваша фамилия?",
            3: "3.Сколько вам лет?",
            4: "4.В какой стране вы проживаете?",
            5: "5.В каком городе вы живете?"
        }


class BotState(StatesGroup):
    name = State()
    surname = State()
    age = State()
    state = State()
    city = State()
    final = State()
