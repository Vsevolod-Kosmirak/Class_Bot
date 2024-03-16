from telebot.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    KeyboardButtonRequestUsers,
)


def select_users_for_ban() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(
            text="Вибери користувачів для бану",
            request_users=KeyboardButtonRequestUsers(request_id=1, max_quantity=5),
        )
    )

    return markup
