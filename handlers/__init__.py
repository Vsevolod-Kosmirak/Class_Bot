import telebot
from telebot.util import content_type_service
from handlers.for_admins import handle1_message, ban_user
from handlers.for_users import send_welcome, bad_word, reaction, command_text


def register_handlers(bot: telebot.TeleBot):
    bot.register_message_handler(
        command_text,
        commands=["chat_name"],
        chat_types=["group", "supergroup"],
        pass_bot=True,
    )
    bot.register_message_handler(
        handle1_message, content_types=content_type_service, pass_bot=True
    )
    bot.register_message_handler(bad_word, bad_words=True, pass_bot=True)
    bot.register_message_handler(send_welcome, commands=["help"], pass_bot=True)
    bot.register_message_reaction_handler(reaction, pass_bot=True)
    bot.register_message_handler(ban_user, pass_bot=True)
