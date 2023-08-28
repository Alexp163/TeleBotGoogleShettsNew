"""
Файл, в котором размещены функции по взаимодействию пользователя, телеграмм-бота,
и гугл-таблицы с данными о пользователе
"""
import telebot
from telebot import types

from working_table import (data_collection_function, data_delivery_fuction,
                           recording_data, recording_delivery_address,
                           recording_transport_company)

TOKEN = '6343158997:AAGPQx1S07jCKYyFZjQUM1XHr84XfdwTwZQ'
bot = telebot.TeleBot(TOKEN)
dict_index_address = {}
dict_customer_data = {}
transport_company = ''


@bot.message_handler(commands=['start'])
def start(
        message: telebot.types.Message):  # запуск приветствия бота и первых кнопок
    """
    Запускает работу телеграм-бота

    Функция, которая запускает работу бота, после ввода сообщения start и
    подгружает меню с 5-ю кнопками, а так же выводит приветствие пользователя.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.chat.id выводит сообщение пользователю в бот
    Returns:
    Функция ничего не возвращает
    """
    user_name = message.from_user.username  # автоопределение имени пользователя запросом в бот
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu = types.KeyboardButton('Главное меню')
    calculator = types.KeyboardButton('Калькулятор')
    personal_account = types.KeyboardButton('Личный кабинет')
    frequent_questions = types.KeyboardButton('Частые вопросы')
    contact_us = types.KeyboardButton('Связь с нами')
    markup.add(main_menu)
    markup.add(calculator)
    markup.add(personal_account)
    markup.add(frequent_questions)
    markup.add(contact_us)
    bot.send_message(message.chat.id, f'Привет! {user_name}',
                     reply_markup=markup)


def enter_cabinet(message: telebot.types.Message):
    """
    Запускает работу личного кабинета

    Функция, которая запускает работу личного кабинета,
    после того как пользователь ввел свои личные данные(или пропустил этот шаг)
    , а так же выводит приветствие пользователя(в личном кабинете).
    Когда пользователь оказывается в личном кабинете запускается меню из
    4-х пунктов, для дальнейшей работы в кабинете.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.chat.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    my_orders = types.KeyboardButton('Мои заказы')
    track_order = types.KeyboardButton('Отследить заказ')
    my_details_for_delivery = types.KeyboardButton('Мои данные для доставки')
    goto_main_menu = types.KeyboardButton('Вернуться в главное меню')
    markup.add(my_orders, track_order, my_details_for_delivery, goto_main_menu)
    bot.send_message(message.chat.id,
                     f'Здравствуйте пользователь, {message.from_user.username}',
                     reply_markup=markup)


def work_cabinet(
        message: telebot.types.Message):  # функция работы в личном кабинете
    """
    Отвечает на запросы пользователя

    Функция, которая выполняет логику взаимодействия непосредственно внутри бота.
    Обеспечивает взаимодействие между разделами бота
    при использовании кнопок меню личного кабинета.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.chat.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Мои заказы':
        bot.send_message(message.chat.id, 'Ваши заказы', reply_markup=markup)
    elif message.text == 'Отследить заказ':
        bot.send_message(message.chat.id, 'Ваш заказ отслеживается',
                         reply_markup=markup)
    elif message.text == 'Мои данные для доставки':
        bot.send_message(message.chat.id, 'Ваши данные для доставки',
                         reply_markup=markup)
    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        main_menu = types.KeyboardButton('Главное меню')
        calculator = types.KeyboardButton('Калькулятор')
        personal_account = types.KeyboardButton('Личный кабинет')
        freq_question = types.KeyboardButton('Частые вопросы')
        markup.add(main_menu)
        markup.add(calculator)
        markup.add(personal_account)
        markup.add(freq_question)
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню',
                         reply_markup=markup)


def answers_questions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    what_is_poizon = types.KeyboardButton('Что такое POIZON?')
    original_products_poizon = types.KeyboardButton(
        'Товары на POIZON точно оригинал?')
    price_difference = types.KeyboardButton('Почему различаются цены?')
    duration_delivery = types.KeyboardButton('Сколько длится доставка?')
    order_payment = types.KeyboardButton('Как оплатить доставку?')
    guarantee_honesty = types.KeyboardButton(
        'Какие гарантии что вы не обманите?')
    order_tracking = types.KeyboardButton('Могу ли я отследить свой заказ?')
    exchange_goods = types.KeyboardButton('Возможно ли поменять товар?')
    size_selection = types.KeyboardButton('Как определиться с размером?')
    delivery_address = types.KeyboardButton('Где я могу забрать посылку?')
    transportation_selection = types.KeyboardButton(
        'Какую транспортную компанию выбрать для доставки по СНГ?')
    return_basic_manu = types.KeyboardButton('Вернуться в главное меню')
    markup.add(what_is_poizon, original_products_poizon, price_difference, duration_delivery, order_payment,
               guarantee_honesty, order_tracking,exchange_goods, exchange_goods, size_selection,
               delivery_address)
    # markup.add(original_products_poizon)
    # markup.add(price_difference)
    # markup.add(duration_delivery)
    # markup.add(order_payment)
    # markup.add(guarantee_honesty)
    # markup.add(order_tracking)
    # markup.add(exchange_goods)
    # markup.add(size_selection)
    # markup.add(delivery_address)
    markup.add(transportation_selection)
    markup.add(return_basic_manu)
    bot.send_message(message.chat.id, 'Выберите интересующий вас вопрос',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def all_messages(
        message: telebot.types.Message):  # алгоритм работы и взаимодействия бота с пользователем
    """
    Обрабатывает ответы на запросы пользователя

    Функция, которая отображает взаимодействие и работу пользователя с кнопками
    бота.
    Из этой функции выполняется вызов функции
    recording_transport_company(user_name, transport_company),
    которая выполняет запись введенных данных в таблицу.
    Функция recording_transport_company(user_name, transport_company)
    запустится после выбора пользователем названия транспортной компании.
    При нажатии кнопки "ввести личные данные" произойдет вызов функции
    start_pro(message) -функция начала записи данных пользователя.
    При нажатии кнопки "пропустить ввод данных" произойдет вызов функции
    get_transport_company(message) - функция фиксации данных о транспортировке
    в гугл-таблицу.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.chat.id выводит сообщения пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    user_name = message.from_user.username  # автоопределение имени пользователя запросом в бот
    data_delivery = data_delivery_fuction(user_name)
    data_collection = data_collection_function(user_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Главное меню':
        bot.send_message(message.chat.id, 'Вы вошли в главное меню',
                         reply_markup=markup)
    elif message.text == 'Частые вопросы':
        bot.send_message(message.chat.id, 'Вы решили узнать о частых вопросах',
                         reply_markup=markup)
        answers_questions(message)
    elif message.text == 'Почта России':
        transport_company = message.text
        recording_transport_company(user_name, transport_company)
        bot.send_message(message.chat.id,
                         'Вы выбрали "Почту России" как транспортную компанию',
                         reply_markup=markup)
        get_index_address(message)
    elif message.text == 'Сдек':
        transport_company = message.text
        recording_transport_company(user_name, transport_company)
        bot.send_message(message.chat.id,
                         'Вы выбрали "Сдек" как транспортную компанию:',
                         reply_markup=markup)
        get_index_address(message)
    elif message.text == 'Боксбери':
        transport_company = message.text
        recording_transport_company(user_name, transport_company)
        bot.send_message(message.chat.id,
                         'Вы выбрали "Боксбери" как транспортную компанию',
                         reply_markup=markup)
        get_index_address(message)
    elif message.text == 'Калькулятор':
        bot.send_message(message.chat.id, 'Вы запустили калькулятор',
                         reply_markup=markup)
    elif message.text == 'Личный кабинет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        enter_personal_data = types.KeyboardButton('Ввести личные данные')
        skip_data_entry = types.KeyboardButton('Пропустить ввод данных')
        return_basic_main = types.KeyboardButton('Вернуться в главное меню')
        markup.add(enter_personal_data)
        markup.add(skip_data_entry)
        markup.add(return_basic_main)
        bot.send_message(message.chat.id,
                         'Здравствуйте! Выберите дальнейшее действие',
                         reply_markup=markup)
    elif message.text == 'Ввести личные данные':
        start_pro(message)
    elif message.text == 'Пропустить ввод данных':
        get_transport_company(message)
    elif message.text == 'Частые вопросы':
        bot.send_message(message.chat.id, 'Вы в разделе: частые вопросы',
                         reply_markup=markup)
    elif message.text == 'Связь с нами':
        bot.send_message(message.chat.id, 'Вы в разделе: связь с нами',
                         reply_markup=markup)
    elif message.text == 'Мои заказы':
        bot.send_message(message.chat.id, 'Ваши заказы', reply_markup=markup)
        bot.send_message(message.from_user.id, data_collection)
    elif message.text == 'Отследить заказ':
        bot.send_message(message.chat.id, 'Ваш заказ отслеживается',
                         reply_markup=markup)
    elif message.text == 'Мои данные для доставки':
        bot.send_message(message.chat.id, 'Ваши данные для доставки',
                         reply_markup=markup)
        bot.send_message(message.chat.id, data_delivery)
    elif message.text == 'Вернуться в главное меню':
        main_menu = types.KeyboardButton('Главное меню')
        calculator = types.KeyboardButton('Калькулятор')
        personal_account = types.KeyboardButton('Личный кабинет')
        frequent_questions = types.KeyboardButton('Частые вопросы')
        markup.add(main_menu)
        markup.add(calculator)
        markup.add(personal_account)
        markup.add(frequent_questions)
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню',
                         reply_markup=markup)
    elif message.text == 'Что такое POIZON?':
        bot.send_message(message.chat.id, 'POIZON - это крупный китайский маркетплейс. На котором можно найти все что '
                                          'угодно, но самый большой его плюс в том, что каждый товар тщательно '
                                          'проверяют на оригинальность и дефекты.')
    elif message.text == 'Товары на POIZON точно оригинал?':
        bot.send_message(message.chat.id, 'Да, ведь каждый товар проходит более 20 проверок. На каждой из стадии '
                                          'проверки его внимательно осматривают. В случае если товар не прошел хотя бы '
                                          'одну проверку POIZON возвращает деньги, следовательно, мы делаем возврат '
                                          'денежных средств.'
                                          'Если товар прошел все проверки, то на нем будет бирка POIZON, отсканировав '
                                          'которую, можно узнать о дате проверки, информации о товаре и тд. Также в '
                                          'коробке/пакете будет лежать сертификат POIZON который так же будет '
                                          'гарантировать, что товар прошел все проверки')
    elif message.text == 'Почему различаются цены?':
        bot.send_message(message.chat.id, 'Цена ниже чем в России, потому что POIZON сотрудничает с мировыми брендами '
                                          'напрямую, ведь у множества брендов крупные фабрики именно в Китае, это '
                                          'позволяет сэкономить на доставке, так как товар преодолевает путь с фабрики '
                                          'бренда до склада POIZON не пересекая границы какого-либо государства, '
                                          'следовательно, не взимаются пошлины.'
                                          'Цена на POIZON так же зависит от спроса на товар, если спрос большой, то и '
                                          'цена растет. Именно поэтому цены могут колебаться раз в пару дней.')
    elif message.text == 'Сколько длится доставка?':
        bot.send_message(message.chat.id, 'Доставка со склада POIZON до склада в Китае зависит от выбранной вами '
                                          'доставки(если есть выбор), в среднем ускоренная 2-3 дня, обычная 5-6 дней. '
                                          'Со склада в Китае до Уссурийска, РФ(ближайший город от границы с Китаем) '
                                          'доставка длится 6-8 дней, в Уссурийске сортировка 1-2 дня, и с Уссурийска '
                                          'отправляем по всему СНГ.'
                                          'Срок доставки с Уссурийска до вашего города зависит от выбранной вами '
                                          'транспортной компании и отдаленности вашего города.')
    elif message.text == 'Как оплатить доставку?':
        bot.send_message(message.chat.id, 'Оплата происходит тремя частями:\n\n'                                    
                                          'Первая и основная - за сам товар, чтобы его выкупить на POIZON (в качестве '
                                          'доказательства мы присылаем чек выкупа).\n\n'
                                          'Вторая часть - доставка до Уссурийска, она оплачивается только тогда, когда '
                                          'взвесят ваш товар на складе в Китае.\n\n'
                                          'Третья часть - доставка с Уссурийска до вашего города оплачивается при '
                                          'получении в отделение транспортной компании.')
    elif message.text == 'Какие гарантии что вы не обманите?':
        bot.send_message(message.chat.id, 'Мы на рынке уже больше года, за это время смогли заработать хорошую репутацию. '
                                          'Есть канал куда публикуем отзывы, к сожалению их оставляет не каждый клиент.'
                                          'Комментарии везде открыты - мы не скрываемся, в крайнем случае можете написать '
                                          'в наш чат, в нем находятся люди которые делали у нас заказ и не раз, они то '
                                          'все и подтвердят.')
    elif message.text == 'Могу ли я отследить свой заказ?':
        bot.send_message(message.chat.id, 'Да, конечно, ваш заказ отслеживается на каждом этапе: от склада POIZON до '
                                          'вашего города, сделать это вы можете в своем личном кабинете, нажав на кнопку'
                                          ' «ОТСЛЕДИТЬ ЗАКАЗ»')
    elif message.text == 'Возможно ли поменять товар?':
        bot.send_message(message.chat.id, 'Вы можете поменять товар на следующий день после заказа. '
                                          'Поменять или вернуть товар после получения товара, к сожалению, невозможно.')
    elif message.text == 'Как определиться с размером?':
        bot.send_message(message.chat.id, 'На каждый товар и бренд идет своя размерная сетка. Если вы не уверены в '
                                          'размере, напишите менеджеру до оформления заказа, он обязательно поможет.')
    elif message.text == 'Где я могу забрать посылку?':
        bot.send_message(message.chat.id, 'Все заказы приходят в отделения транспортных компаний в вашем городе. '
                                          'Мы сотрудничаем с такими компаниями как Сдек, Почта России, Боксбери. '
                                          'Во время оформления заказа менеджер запросит все необходимые данные.')
    elif message.text == 'Какую транспортную компанию выбрать для доставки по СНГ?':
        bot.send_message(message.chat.id, 'Рассчитать примерную стоимость доставки вы можете в нашем калькуляторе.')

def get_index_address(message: telebot.types.Message):
    """
    Запускает ввод индекса и адреса отделения для доставки товара

    Функция, которая запустит начало работы по сбору данных(индекс и адрес
    отделения) о доставке товара для пользователя.
    Передаёт управление в функцию entering_index_address(message),
    в которой будет введен индекс и адрес отделения доставки товара.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.chat.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    dict_index_address[message.chat.id] = {}
    bot.send_message(message.chat.id, 'Введите индекс и адрес отделения')
    bot.register_next_step_handler(message, entering_index_address)


def entering_index_address(message: telebot.types.Message):
    """
    Вводит индекс и адрес отделения для доставки товара

    Функция, которая произведет действие по сбору данных(индекс и адрес
    отделения)
    о доставке товара для пользователя.
    Передаёт управление в функцию welcome_cabinet(message), для перехода в
    личный кабинет.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.chat.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    user_name = message.from_user.username  # автоопределение имени пользователя запросом в бот
    index_address = message.text
    dict_index_address[message.chat.id]['Индекс и адрес'] = index_address
    recording_delivery_address(user_name, dict_index_address)
    welcome_cabinet(message)


def welcome_cabinet(message: telebot.types.Message):
    """
    Переходит в личный кабинет

    Функция, которая создаст кнопку, при нажатии которой, произойдет
    вызов функции enter_cabinet(message) и пользователя перенаправит в личный
    кабинет.

    Args:
    message: discord.Message - аргумент для взаимодействия между пользователем
    и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    my_cabinet = types.KeyboardButton('Перейти в личный кабинет')
    markup.add(my_cabinet)
    bot.send_message(message.from_user.id, 'Спасибо, что ввели данные!',
                     reply_markup=markup)
    enter_cabinet(message)


def start_pro(message: telebot.types.Message):
    """
    Подготавливает к запуску ввода данных пользователя

    Функция запустит сбор данных о пользователе, для дальнейшего сбора данных в
    гугл -таблицу.
    Отправит запрос на запуск следующей функции get_name(message)с помощью метода
    bot.register_next_step_handler(message, get_name), для ввода ФИО пользователя.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    dict_customer_data[message.chat.id] = {}
    bot.send_message(message.from_user.id, 'Введите своё Ф.И.О.')
    bot.register_next_step_handler(message, get_name)


def get_name(message: telebot.types.Message):
    """
    Принимает данные о ФИО пользователя, с последующей обработкой.

    Функция выполнит сбор и обработку данных о ФИО пользователя,
    с добавлением полученных данных в переменную dict_customer_data.
    Отправит запрос на запуск следующей функции get_telephone(message), при
    помощи метода bot.register_next_step_handler(message, get_name), для ввода
    телефона пользователя.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    name = message.text
    dict_customer_data[message.chat.id]['Ф.И.О.'] = name
    bot.send_message(message.from_user.id, 'Введите номер телефона')
    bot.register_next_step_handler(message, get_telephone)


def get_telephone(message: telebot.types.Message):  # функция ввода телефона
    """
    Принимает данные о телефоне пользователя, с последующей обработкой.

    Функция выполнит сбор и обработку данных о телефоне пользователя,
    с добавлением полученных данных в переменную dict_customer_data.
    Отправит запрос на запуск следующей функции get_index(message) при помощи
    метода bot.register_next_step_handler(message, get_name), для ввода индекса
    пользователя.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    telephone = message.text
    dict_customer_data[message.chat.id]['телефон'] = telephone
    bot.send_message(message.from_user.id, 'Введите индекс проживания')
    bot.register_next_step_handler(message, get_index)


def get_index(message: telebot.types.Message):
    """
    Принимает данные об индексе проживания пользователя, с последующей обработкой.

    Функция выполнит сбор и обработку данных об индексе проживания пользователя,
    с добавлением полученных данных в переменную dict_customer_data.
    Отправит запрос на запуск следующей функции get_address(message)при помощи
    метода bot.register_next_step_handler(message, get_name), для ввода адреса
    проживания пользователя.

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    index = message.text
    dict_customer_data[message.chat.id]['индекс'] = index
    bot.send_message(message.from_user.id, 'Введите адрес проживания')
    bot.register_next_step_handler(message, get_address)


def get_address(message: telebot.types.Message):
    """
    Принимает данные о адресе проживания пользователя, с последующей обработкой.

    Функция выполнит сбор и обработку данных о адресе проживания пользователя,
    с добавлением полученных данных в переменную dict_customer_data.
    После обработки всех полученных данных из функций(start_pro(message),
    get_name(message),get_telephone(message),
    get_index(message),get_address(message)) происходит вызов
    функции recording_data(user_name, dict_customer_data)-которая
    запишет полученные данные в гугл-таблицу(колонка "I"-данные получателя).

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    address = message.text
    dict_customer_data[message.chat.id]['адрес'] = address
    user_name = message.from_user.username  # автоопределение имени пользователя запросом в бот
    print(f'словарь с данными покупателя1{dict_customer_data}{user_name}')
    recording_data(user_name, dict_customer_data)
    get_transport_company(message)


def get_transport_company(message: telebot.types.Message):
    """
    Запускает блок кнопок о транспортной компании пользователя

    Функция выполнит запуск блока кнопок, для выбора пользователем транспортной
    компании.
    Выбор пользователя будет обработан в функции all_messages(message) и
    отправлен на запись в таблицу при помощи функции
    recording_transport_company(user_name, transport_company).

    Args:
    message: telebot.types.Message - аргумент для взаимодействия между
    пользователем и ботом.
    message.from_user.id выводит сообщение пользователю в бот.
    Returns:
    Функция ничего не возвращает
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian_post = types.KeyboardButton('Почта России')
    sdek = types.KeyboardButton('Сдек')
    boxbery = types.KeyboardButton('Боксбери')
    markup.add(russian_post)
    markup.add(sdek)
    markup.add(boxbery)
    bot.send_message(message.from_user.id, 'Выберите транспортную компанию',
                     reply_markup=markup)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
