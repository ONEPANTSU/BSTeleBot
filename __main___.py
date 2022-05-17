import json

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
import bsbot_config as config
updater = Updater(token=config.API_TOKEN)
dispatcher = updater.dispatcher

def about():
    return "Для извлечения исходных данных используйте команды:" \
           "/navigators index, где index - номер параметра в таблице навигаторов;"

# функция обработки команды '/start'
def func_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bonch-Science Bot!")

# функция обработки текстовых сообщений
def func_text(update, context):
    text_out = 'Получено сообщение: ' + update.message.text + '\n' + about()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_out)

# функция обработки команды '/navigators'
def func_navigators(update, context):
    if context.args:
        text_reply = get_navigator_data(context.args[0])
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text=text_reply)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='Необходимо указать аргумент команды /navigators')

def get_navigator_data(self, index_param):
    ret = json.dumps("Данные не найдены!( Параметр:{}", ensure_ascii=False)
    index = int(index_param)
    #..........................
    return ret

# функция обработки не распознанных команд
def func_unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Введена неизвестная команда! :c")

# обработчик команды '/start'
start_handler = CommandHandler('start', func_start)
dispatcher.add_handler(start_handler)

# обработчик текстовых сообщений
text_handler = MessageHandler(Filters.text & (~Filters.command), func_text)
dispatcher.add_handler(text_handler)

# обработчик команды '/navigators'
navigators_handler = CommandHandler('navigators', func_navigators)
dispatcher.add_handler(navigators_handler)

# обработчик не распознанных команд
unknown_handler = MessageHandler(Filters.command, func_unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()

# обработчик нажатия Ctrl+C
updater.idle()
