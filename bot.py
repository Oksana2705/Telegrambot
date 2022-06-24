# импортируем необходимые модули библиотеки aiogram и токен бота,
# а так же инициализируем объекты бота и диспетчера
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда, с которой начинается общение пользователя с ботом - /start.
# Научим нашего бота реагировать на эту команду.
# Создаем message_handler и объявляем там функцию ответа

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!\nХочу с вами познакомиться, в каком городе вы проживаете?")


@dp.message_handler(content_types=["text"])
async def text_message(message):
    if message.text.lower() == 'минск':
        await bot.send_message(message.from_user.id, 'Здорово, класивый город, укажите ваш пол (мужской/женский)')
    elif message.text.lower() == 'мужской':
        await bot.send_message(message.from_user.id, 'Йоу, приятно общению!')
    elif message.text.lower() == 'женский':
        await bot.send_message(message.from_user.id, 'Супер, прекрасная половина нас посетила!')
    else:
        await bot.send_message(message.from_user.id, "Что-то не то, подумайте лучше!")

#Чтобы получать сообщения от серверов Telegram воспользуемся поллингом (polling. to poll - опрашивать)
# - постоянным опросом сервера на наличие новых обновлений.
if __name__ == '__main__':
    executor.start_polling(dp)




