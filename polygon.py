import telebot
import sqlite3
import logging
conn = sqlite3.connect('usernames', check_same_thread=False)
cursor = conn.cursor()
BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)

def update_sqlite_table(ids, username): #updating NOW WALLET
    try:
        sqlite_connection = sqlite3.connect('usernames')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update usn set username = ? where id = ?"""
        data = (username, ids)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def db_table_val(ids, username): #updating NOW WALLET
    try:
        sqlite_connection = sqlite3.connect('usernames')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update usn set username = ? where id = ?"""
        data = (username, ids)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



def read_single_row(ids):
    try:
        sqlite_connection = sqlite3.connect('usernames')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sqlite_select_query = """SELECT * from usn where id = ?"""
        cursor.execute(sqlite_select_query, (ids, ))
        print("Чтение одной строки \n")
        record = cursor.fetchone()
        print("ID:", record[0])
        global dbid
        global dbusr
        dbid = record[0]
        dbusr = record[1]
        print("Имя:", record[1])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


@bot.message_handler(content_types=['text'])
def start(message):

    try:
        ids = message.from_user.id
        username = message.from_user.username
        read_single_row(ids)
        if ids == dbid and username == dbusr:
            print("все правильно")

        else:
            ids = message.from_user.id
            username = message.from_user.username

            db_table_val(ids, username)


            f = open('text.txt', 'a')

            ids = message.from_user.id
            username = message.from_user.username
            print(username, "ЕБАШИМ")
            f.write(username + ' ')
            f.write(dbusr + '\n')
            update_sqlite_table(ids, username)




            bot.send_message(message.chat.id, f"ЮЗЕР {message.from_user.first_name} СМЕНИЛ СВОЙ ЛИНК. ЭТО БУДЕТ ЗАПИСАНО")
    except TypeError:
        ids = message.from_user.id
        username = message.from_user.username
        db_table_val(ids, username)


bot.polling(none_stop=True)
f = open('text.txt', 'w')
