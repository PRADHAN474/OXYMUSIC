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
                text="𝙷𝚎𝚕𝙿",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚂", callback_data="settings_helper"
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
                text="𝙷𝚎𝚕𝙿", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝚂𝚞𝚙𝚙𝚘𝚛𝚃 ✨", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚁 🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ 𝙾𝚡𝚢𝚐𝚎𝙽 𝚁𝚘𝚋𝚘𝚃 ❄", url="https://t.me/Blossom_xmusic_bot"
            )
        ],
     ]
    return buttons
