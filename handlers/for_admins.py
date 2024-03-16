import time
from keyboards.admins_kb import select_users_for_ban

import redis

redis_obj = redis.Redis(host="localhost", port=6379)


def handle1_message(message, bot):
    bot.send_chat_action(message.chat.id, "choose_sticker")
    time.sleep(15)
    bot.delete_message(
        message.chat.id,
        message.message_id,
    )


def ban_user(message, bot):
    user_for_ban = int(message.reply_to_message.from_user.id)
    redis_obj.set("BANNED_USERS", user_for_ban)
    bot.reply_to(message, "Забанено")
