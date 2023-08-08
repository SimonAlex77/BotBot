import os

from aiogram import Bot, Dispatcher, executor, types
import time
import logging

import transliterate

TOKEN = os.getenv('TOKEN')

# TOKEN = '6597671936:AAH9YT9nMdwWGj8wWUxTu9hwqclnnYzfNog'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    logging.info(f'{user_id=} {user_fullname=} {time.asctime()}')
    await message.reply(f'Привет, {user_fullname}! Напиши имя русскими буквами и я его преобразую в латинские.')

@dp.message_handler()
async def convert_fio(message: types.Message):
    fio_spl = message.text.split(' ')
    if len(fio_spl) == 3:
        fio_kir = message.text
        fio_lat = transliterate.translit(fio_kir, reversed=True)
        await message.reply(fio_lat)
    else:
        await message.reply("Введите, пожалуйста, на кириллице в формате ФИО.")


if __name__ == '__main__':
    executor.start_polling(dp)