# TelegramBotServey
Telegram bot python aiogram
Прохождение опроса из пяти вопросов. Имя, фамилия, возраст, страна, город. Возраст храним как int.

На старте бот возвращает сообщение приветствие где показывает введенную юзером информацию.
Если юзер ничего не ввел, то просто текст "Привет"
Если юзер завершил опрос, то построчно все ответы. Каждый с новой строки.
К сообщению в окне инлайн кнопка "Начало опроса"

После начала опроса запускается диалог. Вопросы задаются поочередно. Ответ принимается текстом. После обработки ответа следующий вопрос. 
С каждым вопросом возвращается кнопка "На главный экран"
При переходе на главный экран возвращается стартовое сообщение. 

При повторном старте опроса сохраняем состояние и возвращаем юзеру первый не отвеченный вопрос. 

Ответы сохраняются все только на последнем вопросе. Сохранять можно в бд любую, либо в условный словарь. 

При старте опроса, когда все вопросы уже отвечены - возвращаем аллерт, что опрос уже пройден. 
