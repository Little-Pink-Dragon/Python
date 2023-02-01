import logging
import random


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
TOKEN = '5960547305:AAFJolwhv4x0qPsbo_hVdjKfgUuFAzMcCrg'
new_storage = []
number = 0
reply_keyboard = [['/start', '/game'],
                  ['/game_new', '/stop']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)




def start(update, context):
    update.message.reply_text(
        f"Я Game_bot и предлагаю сыграть в игру"
        f"\nЯ загадываю любое число от 1 до 100"
        f"\nТвоя задача угадать это число"
        f"\nНа это у тебя есть 5 попыток"
        f"\n----------Начнем?------------"
        f"\n/game - Начать игру"
        f"\n/stop - Завершить работу бота",
        reply_markup=markup
    )
def game(update, context):
    global number
    update.message.reply_text(f'Прекрасно {update.effective_user.first_name}, тогда начнем')
    number_random = random.randint(1,100)
    number = number_random
    context.bot.send_message(
        update.effective_chat.id,
        f"Я загадал число, теперь твоя задача его угодать"
        f"\nКак думаешь? Какое это число?")
    reply_markup=ReplyKeyboardRemove()
    return 1


def game_one(update, context):
    global choice
    choice = int(update.message.text)
    if choice == number:
        context.bot.send_message(update.effective_chat.id,
            f"Супер, ты отгадал число")
        return 7
    elif number > 50:
         update.message.reply_text(
        f"Не угодал(((, ПОДСКАЗКА: Моё число больше 50" 
        "\nУ тебя есть ещё 4 попытки")
    elif number < 50:
         update.message.reply_text(
        f"Не угодал(((, ПОДСКАЗКА: Моё число меньше 50" 
        "\nУ тебя есть ещё 4 попытки")
    return 2

def game_two(update, context):
    choice = int(update.message.text)
    new_storage.append(choice)
    if choice == number:
        context.bot.send_message(update.effective_chat.id,
            f"Супер, ты отгадал число")
        return 7
    elif choice > number:
         update.message.reply_text(
        f"Опять не угодал, держи ещё подсказку: Твоё число больше, чем я загадал" 
        "\nУ тебя есть ещё 3 попытки")
    elif choice < number:
         update.message.reply_text(
        f"Опять не угодал, держи ещё подсказку: Твоё число меньше, чем я загадал" 
        "\nУ тебя есть ещё 3 попытки")
    return 3

def game_three(update, context):
    remains = number%2
    choice = int(update.message.text)
    new_storage.append(choice)
    if choice == number:
        context.bot.send_message(update.effective_chat.id,
            f"Супер, ты отгадал число")
        return 7
    elif remains == 1:
         update.message.reply_text(
        f"Снова не угодал, моё число нечётное" 
        "\nУ тебя есть ещё 2 попытки")
    elif remains == 0:
         update.message.reply_text(
        f"Снова не угодал, моё число чётное" 
        "\nУ тебя есть ещё 2 попытки")
    return 4

def game_four(update, context):
    choice = int(update.message.text)
    new_storage.append(choice)
    number_three = random.randint(1,4)
    number_four = number + number_three
    if choice == number:
        context.bot.send_message(update.effective_chat.id,
            f"Супер, ты отгадал число")
        return 7
    else: update.message.reply_text(
        f"У тебя остался последний шанс угадать число"
        f"\nПоследняя подсказка: Моё число чуть меньше {number_four}")
    
    return 5


def game_five(update, context):
    choice = int(update.message.text)
    new_storage.append(choice)
    if choice == number:
        context.bot.send_message(update.effective_chat.id,
            f"Супер, ты отгадал число")
        return 7
    else: update.message.reply_text(
        f"Не угадал((, моё число было - {number}")
    return 6

def game_new(update, context):
    context.bot.send_message(update.effective_chat.id,
            f"Ну что же, начнём игру заново"
            f"Введи любое значение")
    return 8

def game_seven(update, context):
    context.bot.send_message(update.effective_chat.id,
            f"Поздравляю тебя!!!"
            f"Желаешь ещё раз сыграть?"
            f"Нажмите /game_new")
    return 8
def game_over (update, context):
    update.message.reply_text(f'Пока 👋 {update.effective_user.first_name}, жду Вас снова)',
    reply_markup=ReplyKeyboardRemove())

def stop(update, context):
    update.message.reply_text(f'Пока 👋 {update.effective_user.first_name}, жду Вас снова)')
    return ConversationHandler.END

game_handler = ConversationHandler(
    entry_points = [CommandHandler("game", game)],
    states = {
        1: [MessageHandler(Filters.text & ~Filters.command, game_one)],
        2: [MessageHandler(Filters.text & ~Filters.command, game_two)],
        3: [MessageHandler(Filters.text & ~Filters.command, game_three)],
        4: [MessageHandler(Filters.text & ~Filters.command, game_four)],
        5: [MessageHandler(Filters.text & ~Filters.command, game_five)],
        6: [MessageHandler(Filters.text & ~Filters.command, game_new)],
        7: [MessageHandler(Filters.text & ~Filters.command, game_seven)],
        8: [MessageHandler(Filters.text & ~Filters.command, game)]
    },
    fallbacks = [CommandHandler("stop", stop)])



def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(game_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("game_over", game_over))
    
    
    updater.start_polling()

    updater.idle()
dispatcher.add_handler(game_handler)

if __name__ == '__main__':
    main()