import os
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def query(update, context):
    try:
        query = int(update.inline_query.query)
    except ValueError:
        return
    if query < 120:
        return
    qty = int(query / 120)  # int() rounds down
    thread_needed = qty * 12
    leather_needed = qty * 2
    withdraw_command = f'/g_withdraw 01 {thread_needed} 20 {leather_needed}'
    craft_command = f'/c_100 {qty}'
    results = list()
    results.append(
        InlineQueryResultArticle(
            id='withdraw',
            title=withdraw_command,
            input_message_content=InputTextMessageContent(withdraw_command)
        )
    )
    results.append(
        InlineQueryResultArticle(
            id='craft',
            title=craft_command,
            input_message_content=InputTextMessageContent(craft_command)
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)
dispatcher = updater.dispatcher
query_handler = InlineQueryHandler(query)
dispatcher.add_handler(query_handler)
print('running')
updater.start_polling()
