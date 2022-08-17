import src.scrap as sc
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import src.glbl_nms


sc.parse_info()
sc.parse_currency()

#Объект бота
bot = Bot(token=src.glbl_nms.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

""""
Создаю кнопки

"""


@dp.message_handler(commands="start")
async def buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = [f'{src.glbl_nms.names[0]}', f'{src.glbl_nms.names[1]}',
                 f'{src.glbl_nms.names[2]}', f'{src.glbl_nms.names[3]}',
                 f'{src.glbl_nms.names[4]}', f'{src.glbl_nms.names[5]}',
                 f'{src.glbl_nms.names[6]}', f'{src.glbl_nms.names[7]}',
                 f'{src.glbl_nms.names[8]}', f'{src.glbl_nms.names[9]}']
    keyboard.add(*buttons_1)
    await message.answer("Какая крипта интересует?", reply_markup=keyboard)


"""
Функции, выводящие информацию конкретной валюты

"""


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[0]}'))
async def crypt_1(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[0]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[0]}']
    await message.answer(f'{src.glbl_nms.names[0]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[1]}'))
async def crypt_2(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[1]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[1]}']
    await message.answer(f'{src.glbl_nms.names[1]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[2]}'))
async def crypt_3(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[2]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[2]}']
    await message.answer(f'{src.glbl_nms.names[2]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[3]}'))
async def crypt_4(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[3]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[3]}']
    await message.answer(f'{src.glbl_nms.names[3]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[4]}'))
async def crypt_5(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[4]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[4]}']
    await message.answer(f'{src.glbl_nms.names[4]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[5]}'))
async def crypt_6(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[5]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[5]}']
    await message.answer(f'{src.glbl_nms.names[5]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[6]}'))
async def crypt_7(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[6]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[6]}']
    await message.answer(f'{src.glbl_nms.names[6]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[7]}'))
async def crypt_8(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[7]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[7]}']
    await message.answer(f'{src.glbl_nms.names[7]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[8]}'))
async def crypt_9(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[8]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[8]}']
    await message.answer(f'{src.glbl_nms.names[8]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


@dp.message_handler(Text(equals=f'{src.glbl_nms.names[9]}'))
async def crypt_10(message: types.Message):
    dicty = src.glbl_nms.dictionary[f'{src.glbl_nms.names[9]}']
    dicty_next = src.glbl_nms.dictionary_next[f'{src.glbl_nms.names[9]}']
    await message.answer(f'{src.glbl_nms.names[9]}\n\n'
                         f'Стоимость в долларах\n{dicty[1]}\n\n'
                         f'Изменение курса в ближайшее время\n{dicty[2]}\n{dicty[3]}\n\n'
                         f'Cтоимость в биткоинах\n{dicty[4]}\n\n'
                         f'Изменение курса в ближайшее время в ВТС\n{dicty[5]}\n{dicty[6]}\n\n'
                         f'Курс относительно других валют\n' + '\n'.join(dicty_next).replace('1', '') +
                         f'\n\nБольше о криптовалюте можете узнать по ссылке\n{dicty[0]}\n\n'
                         )


def start():
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
