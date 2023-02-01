import sqlite3

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters

import A_simple_bot

Dragon_bot = "6104023107:AAHjTLlT2idogAPQimwh2w5dTQMG85BDl4w"

bot = Bot(Dragon_bot)
updater = Updater(Dragon_bot, use_context = True)
dispatcher = updater.dispatcher

conn = sqlite3.connect("subscribers.db", check_same_thread = False)
cursor = conn. cursor()
new_storage = []
 
def start(update, context):
    update.message.reply_text(f'Привет 👋 {update.effective_user.first_name}')
    context.bot.send_message (
        update.effective_chat.id,
        f"Я Telephone directory - bot"
        f"\nКакое действие хотите выполнить?"
        f"\n/all_contacts - Показать все контакты"
        f"\n/search - Найти контакт по имени или фамилии"
        f"\n/new - Добавить новый контакт"
        f"\n/delete - Удалить контакт по ID"
        f"\n/stop - Завершить работу бота"
    )

def all_contacts(update, context):
    data = A_simple_bot.get_contacts(cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f"{data}"
    )

def search(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите имя или фамилию"
        f"\nДля выхода введите /stop"
        f"\n/start - Чтобы вернуться в начальное меню")
    return 1
    

def search_context(update, context):
    item = update.message.text
    data = A_simple_bot.get_contact(item, cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f"{data}"
    )

def stop(update, context):
    update.message.reply_text(f'Пока 👋 {update.effective_user.first_name}, жду Вас снова)')
    return ConversationHandler.END


def new(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите имя контакта")
    return 1

def new_name(update, context):
    name = update.message.text
    new_storage.append(name)
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите фамилию")
    return 2

def new_surname(update, context):
    surname = update.message.text
    new_storage.append(surname)
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите номер телефона")
    return 3

def new_phone(update, context):
    Number = update.message.text
    new_storage.append(Number)
    A_simple_bot.new_contact(new_storage, conn, cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f"Запись добавлена"
        f"\nДля выхода введите /stop"
        f"\n/start - Чтобы вернуться в начальное меню")
    new_storage.clear()   


def delete_contact(update, context):
    id_contact = update.message.text
    msg = A_simple_bot.delete(id_contact, conn, cursor)
    context.bot.send_message(
        update.effective_chat.id, msg)

def delete(update, context):
    context.bot.send_message(
        update.effective_chat.id, 
        f"Введите ID контакта")
    return 1

def get_handler(command, func, func1):
    hand = ConversationHandler(
    entry_points = [CommandHandler(command, func)],
    states = {
        1: [MessageHandler(Filters.text & ~Filters.command, func1)],
    },
    fallbacks = [CommandHandler("stop", stop)]
    )
    return hand

new_handler = ConversationHandler(
    entry_points = [CommandHandler("new", new)],
    states = {
        1: [MessageHandler(Filters.text & ~Filters.command, new_name)],
        2: [MessageHandler(Filters.text & ~Filters.command, new_surname)],
        3: [MessageHandler(Filters.text & ~Filters.command, new_phone)],
    },
    fallbacks = [CommandHandler("stop", stop)]
)

search_handler = get_handler("search", search, search_context)
delete_handler = get_handler("delete", delete, delete_contact)

start_handler = CommandHandler("start", start)
back_handler = CommandHandler("back", start)
show_handler = CommandHandler("all_contacts", all_contacts)
stop_handler = CommandHandler("stop", stop)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(new_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(stop_handler)
updater.start_polling()
updater.idle()
conn.close()