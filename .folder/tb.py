from telegram import Update, Bot
from telegram .ext  import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from Key import TOKEN


bot  = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher




def start (update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")

def info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды:
                             /sum - сложение
                             /sub - вычитание
                             /mult - умножение
                             /dif - деление""")

    context.bot.send_message(update.effective_chat.id, f'Введите команду и два числа через пробел  ')
    return operation


def operation(update, context):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    if items[0] == '/sum':
        context.bot.send_message(update.effective_chat.id, f'{x} + {y}={x+y}')
    elif items[0] == '/sub':
        context.bot.send_message(update.effective_chat.id, f'{x} - {y}={x-y}')
    elif items[0] == '/mult':
        context.bot.send_message(update.effective_chat.id, f'{x} * {y}={x*y}')
    elif items[0] == '/dif':
        context.bot.send_message(update.effective_chat.id, f'{x} / {y}={x/y}')
    context.bot.send_message(update.effective_chat.id, f'Если хотите продолжить вычисления, напишите /info')    
    

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, operation)
#unknown_handler = MessageHandler(Filters.command, unknown)  # /game


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
#dispatcher.add_handler(conv_handler)
#dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


print('server started')
updater.start_polling()
updater.idle()