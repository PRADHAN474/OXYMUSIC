from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙰𝚍𝚖𝚒𝚗𝚂",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝙰𝚞𝚝𝙷",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝙱𝚕𝚊𝚌𝚔𝙻𝚒𝚜𝚝𝚂",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝙱𝚛𝚘𝚊𝙳𝚌𝚊𝚜𝚃",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝙶𝚋𝚊𝙽",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="𝙻𝚢𝚛𝚒𝚌𝚂",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝙿𝚒𝙽𝙶",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="𝙿𝚕𝚊𝚈",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="𝙿𝚕𝚊𝚢𝙻𝚒𝚜𝚝𝚂",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝚅𝚒𝚍𝚎𝙾𝙲𝚑𝚊𝚝𝚂",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="𝚂𝚝𝚊𝚛𝚃",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="𝚂𝚞𝚍𝙾",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ ʜᴇʟᴩ ❄",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
