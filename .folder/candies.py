# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
)

NUMBER_PLAYER1 = range(1)


number = 112
count1 = 0
count2 = 0

def start(update, _):
    user = update.message.from_user
    update.message.reply_text(
        f'Добро пожаловать, {user.username}!Игра в конфеты начинается!')
    update.message.reply_text('Введите количество конфет, которое возьмете, от 1 до 28')
    return NUMBER_PLAYER1


def  main_game(update, _):
    global number, count1, count2
    number_player1 = update.message.text
    number_player1 = int(number_player1)
    if number_player1 < 0 or number_player1 > 28:
        update.message.reply_text('Введите количество конфет от 1 до 28')
        return main_game
    else:
        count1 += 1
        number = number - number_player1
        number_player2 = 28 - number_player1
        count2 += 1
        number  = number - number_player2
        update.message.reply_text(f'Второй игрок ввел {number_player2} конфет. Осталось {number} конфет')
        if number == 0:
            if count1 > count2:
                update.message.reply_text('Вы проиграли')
                return ConversationHandler.END
            else:
                update.message.reply_text('Поздравляем! Вы выиграли!')
                return ConversationHandler.END
        else:
            return main_game
        
            

            


def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пишите.',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END                  

        
        

