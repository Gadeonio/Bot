import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, InlineQueryHandler

from pathlib import Path
from os import chdir

import model.my_token
from model.rooms import BaseReservation

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

reservation = BaseReservation()
reservation.read_in_json_file()


async def reservate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 2:
        start_time, end_time = tuple(context.args)
        check = reservation.add_reservation(start_time, end_time=end_time)
        if check:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Успешно резервирована комната")
            reservation.save_in_json_file()
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Ошибка в резервировании")




async def reservation_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Moment please")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(reservation))


if __name__ == '__main__':
    application = ApplicationBuilder().token(model.my_token.get_token()).build()
    reservate_handler = CommandHandler('reservate', reservate)
    reservation_info_handler = CommandHandler('reservation_info', reservation_info)

    application.add_handler(reservate_handler)
    application.add_handler(reservation_info_handler)


    application.run_polling()
