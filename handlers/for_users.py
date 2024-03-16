from telebot.util import extract_arguments
from telebot import TeleBot
from telebot.types import Message


def send_welcome(message, bot):
    bot.send_message(
        message.chat.id,
        f"Привіт {message.from_user}.\n"
        f"Я бот, місією якого буде доповнити життя цієї групи."
        f"Покищо я на стадії розробки",
    )


def bad_word(message, bot):
    bot.send_message(
        message.chat.id,
        f"Я знаю все про тебе:\n{message.from_user},"
        f"\nТому попрошу матюкатись по українськи",
    )


def reaction(react, bot):
    emoji = react.new_reaction[0].emoji
    print(emoji)
    bot.set_message_reaction(
        chat_id=react.chat.id,
        message_id=react.message_id,
        reaction=[react.new_reaction[0]],
    )


def command_text(message: Message, bot: TeleBot):
    print(message)
    bot.set_chat_title(message.chat.id, title=extract_arguments(message.text))
