import telegram

from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep
from sql_cons import *
import sqlite3
def start(update, context):
    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name

    context.bot.send_message(chat_id= user_id, text='{}, 👋🙃'.format(f_name))
    sleep(1)
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    stage_update = cur.execute(stage.format(user_id)).fetchall()

    try:
        TG_ID = TG_ID[0][0]
        if TG_ID== 957531477:
            id = 957531477
            context.bot.send_message(chat_id=id, text='Здраствуйте Авазбек,ваш персональный бот для продвижения вашего бизнеса.\n Я вам буду вам отправлять анкету людей желающих ходить к вашим курсам по английскому языку. Я умею:\n ')
    except Exception:
        pass
    if TG_ID == user_id:
        context.bot.send_message(chat_id=user_id, text='Вы уже в нашей базе данных')
        sleep(1)
        context.bot.send_message(chat_id=user_id, text='Siz bizning malumotlar bazamizda borsiz')
        sleep(1)
    if user_id != TG_ID:
        cur.execute(first_insert.format(user_id,1))
        connect.commit()
        sleep(1)
        knopka_lang = [
            InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni taglang:',
                              reply_markup=InlineKeyboardMarkup([knopka_lang]))
        sleep(1)







def next_func(update, context):
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    message = update.message.text
    message = str(message)
    try:
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]


        if message.lower() == 'davom etish>>>' and stage_ == 2 or message.lower() == 'далее>>>' and stage_ == 2:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][0])
            sleep(1)
            context.bot.send_message(chat_id=user_id, text=dct[lang_][1])
            sleep(1)

            cur.execute(stagee.format('{}', user_id).format(3))
            connect.commit()
        if stage_== 3:
            message1 = update.message.text
            cur.execute(upd_name.format(message1, user_id))
            connect.commit()
            context.bot.send_message(text=dct[lang_][3], chat_id=user_id)
            sleep(1)
            cur.execute(stagee.format('{}', user_id).format(4))
            connect.commit()


        if stage_ ==4 and stage_ >3 and stage_ <5 :
           name = cur.execute(select_name.format(user_id)).fetchall()
           name = name[0][0]
           b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

           context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(name),
                    reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))
           sleep(1)
           cur.execute(stagee.format('{}', user_id).format(5))
           connect.commit()
           print(3)

    except Exception:
         pass

def get_contac(update, context):
        user_id = update.message.chat_id
        num = update.message.contact.phone_number
        name = update.message.from_user.first_name
        num = str(num)
        conn = sqlite3.connect('table_0f_tables.sqlite')
        cur = conn.cursor()
        cur.execute(update_phone_num.format(num, user_id))
        conn.commit()
        cur.execute(stagee.format('{}', user_id).format(5))
        conn.commit()

        stage_ = cur.execute(stage.format(user_id)).fetchall()
        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        conn.commit()
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        if stage_ == 5:
            level_list = [
                InlineKeyboardButton( text='Beginner', callback_data='biginner'),
                InlineKeyboardButton(text='Elementary', callback_data='elementary'),
                InlineKeyboardButton(text='Pre-intermediate', callback_data='preintermedite'),
                InlineKeyboardButton(text='Intermediate',callback_data='intermediate'),
                InlineKeyboardButton(text='Pre-ielts', callback_data='preielts'),
                InlineKeyboardButton(text='Ielts', callback_data='ielts')
            ]

            name = cur.execute(select_name.format(user_id)).fetchall()
            name = name[0][0]

            context.bot.send_message(chat_id=user_id, text=dct[lang_][5].format(name),
                                     reply_markup=InlineKeyboardMarkup([level_list]))
            sleep(1)

            cur.execute(stagee.format('{}', user_id).format(6))
            conn.commit()





def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(text='нажмите на кнопку далее...' , chat_id=user_id, reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True))
    sleep(1)
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='davom etamish tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True))
    sleep(1)










    conn.commit()
    level_ = cur.execute(select_level.format(user_id)).fetchall()
    level_ = level_[0][0]
    conn.commit()

def biginner(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    cur.execute(get_level.format(level_dct[1], user_id))
    cur.execute(get_ageid.format(400000, user_id))
    connect.commit()
    if stage_ == 6:

        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        name = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        cost = cur.execute(select_age.format(user_id)).fetchall()
        select_level_ = cur.execute(select_level.format(user_id)).fetchall()
        connect.commit()
        select_level_ = select_level_[0][0]
        cost = cost[0][0]
        num_ = num_[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=user_id)
        sleep(1)
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=574596333)
        sleep(1)


def elementary(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    cur.execute(get_level.format(level_dct[2], user_id))
    cur.execute(get_ageid.format(400000, user_id))
    connect.commit()
    if stage_ == 6:

        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        name = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        cost = cur.execute(select_age.format(user_id)).fetchall()
        select_level_ = cur.execute(select_level.format(user_id)).fetchall()
        connect.commit()
        select_level_ = select_level_[0][0]
        cost = cost[0][0]
        num_ = num_[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=user_id)
        sleep(1)
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=574596333)
        sleep(1)

def preintermedite (update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    cur.execute(get_level.format(level_dct[3], user_id))
    cur.execute(get_ageid.format(400000, user_id))
    connect.commit()
    if stage_ == 6:

        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        name = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        cost = cur.execute(select_age.format(user_id)).fetchall()
        select_level_ = cur.execute(select_level.format(user_id)).fetchall()
        connect.commit()
        select_level_ = select_level_[0][0]
        cost = cost[0][0]
        num_ = num_[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=user_id)
        sleep(1)
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=574596333)
        sleep(1)


def intermediate (update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    cur.execute(get_level.format(level_dct[4], user_id))
    cur.execute(get_ageid.format(450000, user_id))
    connect.commit()
    if stage_ == 6:

        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        name = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        cost = cur.execute(select_age.format(user_id)).fetchall()
        select_level_ = cur.execute(select_level.format(user_id)).fetchall()
        connect.commit()
        select_level_ = select_level_[0][0]
        cost = cost[0][0]
        num_ = num_[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=user_id)
        sleep(1)
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=574596333)
        sleep(1)

def preielts (update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    cur.execute(get_level.format(level_dct[5], user_id))
    cur.execute(get_ageid.format(450000, user_id))
    connect.commit()
    if stage_ == 6:

        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        name = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        cost = cur.execute(select_age.format(user_id)).fetchall()
        select_level_ = cur.execute(select_level.format(user_id)).fetchall()
        connect.commit()
        select_level_ = select_level_[0][0]
        cost = cost[0][0]
        num_ = num_[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=user_id)
        sleep(1)
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=574596333)
        sleep(1)

def ielts (update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    cur.execute(get_level.format(level_dct[6], user_id))
    cur.execute(get_ageid.format(450000, user_id))
    connect.commit()
    if stage_ == 6:
        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        name = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        cost = cur.execute(select_age.format(user_id)).fetchall()
        select_level_ = cur.execute(select_level.format(user_id)).fetchall()
        connect.commit()
        select_level_ = select_level_[0][0]
        cost = cost[0][0]
        num_ = num_[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=user_id)
        sleep(1)
        context.bot.send_message(text=dct[lang_][7].format(name, num_, select_level_, cost), chat_id=574596333)
        sleep(1)


def adm(update,context):
    user_id = update.message.chat_id
    if user_id == 574596333:
        text = update.message.caption
        photo_id = update.message.photo[-1].file_id
        file = context.bot.getFile(photo_id)
        file.download('Photo_base/Picture.jpeg')
        if text == None:
            pass
        else:
            connect = sqlite3.connect('table_0f_tables.sqlite')
            cur = connect.cursor()
            id =  cur.execute('''
            SELECT TG_ID
            FROM Users
            WHERE TG_ID !=0
            ''').fetchall()
            for e in id:
                e = e[0]
                print(e)
                context.bot.send_photo(photo= open('Photo_base/Picture.jpeg','rb'), chat_id=e, caption=text)
                sleep(1.5)

def adm_doc (update,context):
    user_id = update.message.chat_id
    if user_id == 574596333:
        text = update.message.caption
        photo_id = update.message.document.file_id
        file = context.bot.getFile(photo_id)
        file.download('Doc_base/Document.docx')
        if text == None:
            pass
        else:
            connect = sqlite3.connect('table_0f_tables.sqlite')
            cur = connect.cursor()
            id =  cur.execute('''
            SELECT TG_ID
            FROM Users
            WHERE TG_ID !=0
            ''').fetchall()
            for e in id:
                e = e[0]
                print(e)
                context.bot.send_document(document= open('Doc_base/Document.docx','rb'), chat_id=e, caption=text)
                sleep(1.5)


