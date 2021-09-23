from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from func import *
from telegram.ext import callbackqueryhandler
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(CallbackQueryHandler(pattern='biginner', callback=biginner))
dis.add_handler(CallbackQueryHandler(pattern='elementary', callback=elementary))
dis.add_handler(CallbackQueryHandler(pattern='preintermedite', callback=preintermedite))
dis.add_handler(CallbackQueryHandler(pattern='intermediate', callback=intermediate))
dis.add_handler(CallbackQueryHandler(pattern='preielts', callback=preielts))
dis.add_handler(CallbackQueryHandler(pattern='ielts', callback=ielts))
dis.add_handler(MessageHandler(Filters.document, adm_doc))
dis.add_handler(MessageHandler(Filters.photo, adm))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))

upd.start_polling(drop_pending_updates=True)
