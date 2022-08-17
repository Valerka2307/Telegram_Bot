import requests
from bs4 import BeautifulSoup
import numpy as np
import src.glbl_nms

"""
Проверка ссылки на наличие пробелов

"""


def checking_for_spaces(link):
    if ' ' in link:
        link1 = link.split()
        link = '%20'.join(link1)
        return link
    else:
        link = link
        return link

"""

Парсинг основной страницы сайта:

    -Название криптовалюты;
    -Стоимость в долларах;
    -Изменение курса за 12 часов и 7 дней;
    -Изменение курса за 12 часов и 7 дней в биткоинах;
    -Ссылку на страницу выбранной криптовалюты;

"""


def parse_info():
    for block in src.glbl_nms.BLOCKS:

        search_teg = block.find('a')
        name = src.glbl_nms.soup.find('a', href=f'{search_teg.get("href")}')
        link = f'https://bitinfocharts.com/ru/crypto-kurs/{search_teg.get("href")}'
        new_link = checking_for_spaces(link)

        search_block = block.find('td')
        short_name = search_block.get("data-val")

        variable = block.find('a', {'class' : 'conv_cur'})

        change = block.find_all_next('span')

        full_name = f'{short_name}({name.text})'

        #цена в BTC
        value_btc = block.find('td', {'class' : 'hidden-phone s6'})
        value_btc = value_btc.get("data-val")

        src.glbl_nms.names.append(full_name)
        #Достаю из списка change текст из нужной информацией
        src.glbl_nms.dictionary[full_name] = [new_link, variable.text, change[1].text, change[2].text,
                                 value_btc, change[4].text, change[5].text]

"""
Парсинг страницы криптовалюты:
    Курс относительно других валют
    
"""


def parse_currency():
    for block in src.glbl_nms.BLOCKS:

        search_teg = block.find('a')
        link = f'https://bitinfocharts.com/ru/crypto-kurs/{search_teg.get("href")}'
        new_url = checking_for_spaces(link)

        cripta_next = requests.get(new_url)
        soup_next = BeautifulSoup(cripta_next.text, 'lxml')
        exchange_rate = soup_next.findAll('span', {'class' : 'text-success'}, limit=6)

        for rates in exchange_rate:
            src.glbl_nms.currency.append(rates.text)

    splits = np.array_split(src.glbl_nms.currency, 10)
    for array in splits:
        src.glbl_nms.currency_1.append(list(array))

    for i in range(10):
        src.glbl_nms.dictionary_next[src.glbl_nms.names[i]] = src.glbl_nms.currency_1[i]
