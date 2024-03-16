# from telebot import TeleBot
# from telebot.types import Message
# from telebot.handler_backends import BaseMiddleware, CancelUpdate
#
#
# bot = TeleBot(
#     "6518329559:AAEyOQI7mWyaz_rlh8foRo9ush3m6S0weTk", use_class_middlewares=True
# )
# BANNED_USERS = [80564738]
#
#
# class BanedMiddleware(BaseMiddleware):
#     def __init__(self):
#         super().__init__()
#         self.update_types = ["message"]
#
#     def pre_process(self, message, data):
#         if message.from_user.id in BANNED_USERS:
#             bot.delete_message(message.chat.id, message.id)
#             return CancelUpdate()
#
#     def post_process(self, message, data, exception=None):
#         pass
#
#
# @bot.message_handler(commands=["start"])
# def start(message: Message, data: dict):
#     bot.send_message(message.chat.id, data["foo"])
#     data["foo"] = "Опрацьовано"
#
#
# bot.setup_middleware(YourMiddleware())
# bot.infinity_polling()
import redis

redis_obj = redis.Redis(host="localhost", port=6379)

result = redis_obj.get("first_name")
print(result)
