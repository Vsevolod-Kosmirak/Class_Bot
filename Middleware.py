from telebot import TeleBot
from telebot.types import Message
from telebot.handler_backends import BaseMiddleware


bot = TeleBot(
    "6518329559:AAEyOQI7mWyaz_rlh8foRo9ush3m6S0weTk", use_class_middlewares=True
)


class YourMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.update_types = ["message"]

    def pre_process(self, message, data):
        data["foo"] = "Привіт"
        print(data["foo"])

    def post_process(self, message, data, exception=None):
        print(data["foo"])
        if exception:
            print(exception)


@bot.message_handler(commands=["start"])
def start(message: Message, data: dict):
    bot.send_message(message.chat.id, data["foo"])
    data["foo"] = "Опрацьовано"


bot.setup_middleware(YourMiddleware())
bot.infinity_polling()
