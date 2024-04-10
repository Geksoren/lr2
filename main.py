from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text # импорт для обработки кнопок

from glob import glob # для выгрузки картинок
from random import choice

def Botik():
    bot = Bot(token="7094998823:AAGRt_yX8Gfs1QXtmx9Q-914uvYWbS7qRS8")  # Объект бота
    dp = Dispatcher(bot)  # Диспетчер - позволяет отслеживать обновления

    buttons = ["Мотивация", "Информация"]
    list_images = glob('images/*')  # лист со названиями всех картинок

    # message_handler — это декоратор, который реагирует на входящие сообщения и содержит в себе функцию ответа
    @dp.message_handler(commands=['start'])
    async def process_start_command(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*buttons)
        await message.answer("Привет!\n"
                             "Я мотивационный бот, который будет поддерживать тебя!\n"
                             "Нажми на кнопку \"Мотивация\", чтобы получить картинку", reply_markup=keyboard)

    @dp.message_handler(Text(equals="Мотивация"))
    async def process_motivation_button (message: types.Message):
        picture = choice(list_images)
        await bot.send_photo(chat_id=message.chat.id, photo=open(picture, 'rb'))

    @dp.message_handler(Text(equals="Информация"))
    async def process_start_command(message: types.Message):
        await message.reply("Я мотивационный бот\nМотивация должна быть всегда\nМотивацию надо подняяяяять\n"
                            "Автор: Наталья Л. ИВТ-232")
    # message.reply - отвечает на полученное сообщение (делает "ответ")
    # message.answer - просто отвечает

    @dp.message_handler(lambda message: not any(button in message.text for button in buttons))
    async def process_start_command(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*buttons)
        await message.answer("Чтобы воспользоваться ботом, нажмите на кнопки", reply_markup=keyboard)


    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=False)  # будет копить сообщения
                                 # skip_updates - пропускать сообщения, которые были отправлены в момент отключения бота

Botik()