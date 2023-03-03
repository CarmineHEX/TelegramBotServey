from aiogram import executor, types
from bot_data import BotData
from creature_button import CreatureButton
from aiogram.dispatcher import FSMContext
from bot_data import BotState

bd = BotData()
cr = CreatureButton()
bs = BotState()


@bd.dp.message_handler(state='*', commands=['start'])
async def start_handler(message: types.Message):
    if bd.count_answer == 1:
        await message.answer("Привет")
        await cr.create_button(message, "Начать опрос", "Нажмите кнопку, чтобы начать опрос")
    elif bd.count_answer <= 6:
        await  message.answer("Привет")
        await cr.create_button(message, "Продолжить опрос", "Нажмите кнопку, чтобы продолжить опрос")
    else:
        await  message.answer("Вы уже ответили на опрос")


@bd.dp.callback_query_handler(text='name_servey')
async def name_servey(call: types.CallbackQuery):
    await bs.name.set()
    await cr.create_button(call.message, "На главный экран", bd.questions[bd.count_answer])
    bd.count_answer += 1


@bd.dp.message_handler(state=bs.name)
async def surname_servey(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await bs.surname.set()
    await cr.create_button(message, "На главный экран", bd.questions[bd.count_answer])
    bd.count_answer += 1


@bd.dp.message_handler(state=bs.surname)
async def age_servey(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await bs.age.set()
    await cr.create_button(message, "На главный экран", bd.questions[bd.count_answer])
    bd.count_answer += 1


@bd.dp.message_handler(state=bs.age)
async def state_servey(message: types.Message, state: FSMContext):
    if str.isnumeric(message.text):
        await state.update_data(age=int(message.text))
        await bs.state.set()
        await cr.create_button(message, "На главный экран", bd.questions[bd.count_answer])
        bd.count_answer += 1
    else:
        await message.answer("Ошибка ввода:Введите число ")


@bd.dp.message_handler(state=bs.state)
async def city_servey(message: types.Message, state: FSMContext):
    await state.update_data(state=message.text)
    await bs.final.set()
    await cr.create_button(message, "На главный экран", bd.questions[bd.count_answer])
    bd.count_answer += 1


@bd.dp.message_handler(state=bs.final)
async def city_servey(message: types.Message, state: FSMContext):
    bd.count_answer += 1
    await state.update_data(city=message.text)
    bd.answers = await state.get_data()
    await message.answer(f"Имя: {bd.answers['name']}\n"
                         f"Фамилия: {bd.answers['surname']}\n"
                         f"Возраст: {bd.answers['age']}\n"
                         f"Страна: {bd.answers['state']}\n"
                         f"Город: {bd.answers['city']}"
                         )
    await cr.create_button(message, "На главный экран", "Конец опроса")
    await state.finish()


@bd.dp.callback_query_handler(state='*', text='home')
async def start_handler(call: types.CallbackQuery):
    if bd.count_answer == 1:
        await call.message.answer("Привет")
        await cr.create_button(call.message, "Начать опрос", "Нажмите кнопку, чтобы начать опрос")
    elif bd.count_answer <= 6:
        await  call.message.answer("Привет")
        await cr.create_button(call.message, "Продолжить опрос", "Нажмите кнопку, чтобы продолжить опрос")
    else:
        await  call.message.answer("Вы уже ответили на опрос")


@bd.dp.callback_query_handler(text='continue_servey', state='*')
async def continue_servey(call: types.CallbackQuery):
    await cr.create_button(call.message, "На главный экран", bd.questions[bd.count_answer - 1])


if __name__ == '__main__':
    executor.start_polling(bd.dp)
