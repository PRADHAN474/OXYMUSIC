from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💫ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ💫",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇𝐄𝐋𝐏",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💫ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ💫",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇𝐄𝐋𝐏", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ✨", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ 𝐎𝐗𝐘𝐆𝐄𝐍 𝐑𝐎𝐁𝐎𝐓 ❄", url="https://t.me/OXYGENMUSIC_BOT"
            )
        ],
     ]
    return buttons
