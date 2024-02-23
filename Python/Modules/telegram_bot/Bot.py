from typing import Final
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# from aiogram.types import ReplyKeyboardMarkupe

# from telegram.TelegramObject import KeyboardButton

token: Final = ""
bot_username: Final = ""

b1 = KeyboardButton("button1")
b2 = KeyboardButton("button2")
l1 = [b1, b2]
l2 = [l1]

keyboard_reply = ReplyKeyboardMarkup(
    keyboard=l2, resize_keyboard=True, one_time_keyboard=True
)
######
from functools import wraps
import logging

# import requests

allowed_users = list()  # List of user_id of authorized users

fhandle = open("./telegram_bot/users_id.txt")


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        for l in fhandle:
            l = l.strip()
            allowed_users.append(int(l))
        print(allowed_users)

        sender_id = update.message.from_user.id
        date = update.message.date
        sender_firstname = update.message.from_user.first_name
        sender_lastname = update.message.from_user.last_name
        m_id = update.message.message_id
        sender_username = update.message.from_user.username
        msg = update.message.text
        is_bot = update.message.from_user.is_bot
        sender_name = update.message.from_user.full_name
        msg_type = update.message.chat.type
        chat_id = update.message.chat.id

        logging.basicConfig(
            level=logging.INFO, filename="./telegram_bot/Bot_log.log", filemode="a"
        )
        logging.disable(logging.NOTSET)
        logging.info(
            f"User id:({sender_id}) Is bot:({is_bot}) Username:({sender_username}) Name:({sender_name}) First name:({sender_firstname}) Last name:({sender_lastname}) Message id:({m_id}) Message type:({msg_type}) Chat id:({chat_id}) Message:({msg}) Date:({date})"
        )
        logging.disable(logging.INFO)

        print(
            f"User id:({sender_id}) Is bot:({is_bot}) Username:({sender_username}) Name:({sender_name}) First name:({sender_firstname}) Last name:({sender_lastname}) Message id:({m_id}) Message type:({msg_type}) Chat id:({chat_id}) Message:({msg}) Date:({date})"
        )

        user_id = update.effective_user.id
        # chat_id = update.message.chat.id
        if user_id not in allowed_users:
            # print("Unauthorized access denied for {}.".format(user_id))
            # message = "Access denied"

            # url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
            # print(requests.get(url).json())
            # return
            return update.message.reply_text(f"Access denied for user id {user_id}")
        return func(update, context, *args, **kwargs)

    return wrapped


######

# Commands


@restricted
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! This is a test bot",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=l2, resize_keyboard=True, one_time_keyboard=True
        ),
    )


@restricted
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("A test bot, test me!")  # type:ignore


@restricted
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command")  # type:ignore


# Responses


# @restricted
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hi!"

    if "how are you" in processed:
        return "I'm good"

    if "i love python" in processed:
        return "Me too"

    return "I don't understand"


@restricted
async def handle_message(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type  # type:ignore
    text: str = update.message.text  # type:ignore

    print(
        f"User ({update.message.chat.id}) in {message_type}: '{text}'"  # type:ignore
    )  # Debugging
    if message_type == "group" or message_type == "supergroup":
        if bot_username in text:
            new_text: str = text.replace(bot_username, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot:", response)  # Debugging

    await update.message.reply_text(response)  # type:ignore


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


# Great tutorial! There's one thing I want to add though. Your implementation of error handler lacks information on a line of the problem. After passing around with GPT-4 for a while I found a solution to get more information:


# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     tb = sys.exc_info()
#     line_number = traceback.extract_tb(tb)[-1][1]
#     exc_type, exc_value, exc_traceback = sys.exc_info()
#     error_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
#     print(f"Update {update} caused error {context.error}:\n{''.join(error_traceback)}")


if __name__ == "__main__":
    print("Starting Bot...")
    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(
        CommandHandler("start", start_command)
    )  # , filters.User(user_id=u_id)))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)  # type:ignore

    # Polling
    print("Polling...")
    app.run_polling(poll_interval=3)
