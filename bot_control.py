import os
import time

import telebot
import fastapi
import uvicorn

from telebot import custom_filters, BaseMiddleware, CancelUpdate, apihelper
from telebot import types, util
import dotenv
from telebot.custom_filters import (
    SimpleCustomFilter,
    AdvancedCustomFilter,
    IsAdminFilter,
)
from telebot.types import Message
import handlers
from telebot.util import update_types, extract_arguments
import redis

WEBHOOK_HOST = "https://enabling-louse-shining.ngrok-free.app"

dotenv.load_dotenv()


bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

app = fastapi.FastAPI()


@app.post("/mybot")
def process_webhook(update: dict):
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


redis_obj = redis.Redis(host="localhost", port=6379)

BANNED_USERS = redis_obj.set("BANNED_USERS", "")


@app.post("/")
@app.get("/")
def hello():
    return "Hello World!"


@bot.message_handler(commands=["start"])
def start_action(message: Message) -> None:
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Привіт, {message.from_user.first_name}. Радий вітати тебе в боті.\n"
        f"Можеш вибрати одну з дій за допомогою кнопок",
    )


class BanedMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.update_types = ["message"]

    def pre_process(self, message, data):
        pass
        # if message.from_user.id in int.from_bytes(
        #     redis_obj.get("BANNED_USERS"), byteorder="big", signed=False
        # ):
        #     bot.delete_message(message.chat.id, message.id)
        #     return CancelUpdate()

    def post_process(self, message, data, exception=None):
        pass


class BadWordsFilter(SimpleCustomFilter):
    key = "bad_words"

    def check(self, message: Message) -> bool:
        words = ["бляха", "блін"]
        for word in words:
            if word in message.text:
                return True

        return False


class HelloFilter(AdvancedCustomFilter):
    key: str = "hello_word"

    def check(self, message: Message, hello: str) -> bool:

        if isinstance(hello, str):
            return message.from_user.text == hello

        return False


# apihelper.ENABLE_MIDDLEWARE = True

handlers.register_handlers(bot)
bad_words = ["бляха", "блін"]


# bot.add_custom_filter(BadWordsFilter())
# bot.add_custom_filter(IsAdminFilter(bot))
# bot.setup_middleware(BanedMiddleware())
bot.set_webhook(url=f"{WEBHOOK_HOST}/mybot", allowed_updates=telebot.util.update_types)

uvicorn.run(app, port=5000)
