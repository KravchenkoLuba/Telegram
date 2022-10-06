import candies as can
from Key import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', can.start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            can.NUMBER_PLAYER1: [MessageHandler(Filters.text & ~Filters.command, can.main_game)],
            can.main_game:[MessageHandler(Filters.text & ~Filters.command, can.main_game)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', can.cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

