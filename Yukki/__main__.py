#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES
from YukkiMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
home_text_pm = f"""𝙃𝙚𝙡𝙡𝙤,
𝙈𝙮 𝙣𝙖𝙢𝙚 𝙞𝙨 🧚 𝙆𝙐𝙏𝙏𝙔 𝘼𝙉𝙂𝙀𝙇 🧚.
𝘼 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙈𝙪𝙨𝙞𝙘+𝙑𝙞𝙙𝙚𝙤 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝙗𝙤𝙩 𝙬𝙞𝙩𝙝 𝙨𝙤𝙢𝙚 𝙪𝙨𝙚𝙛𝙪𝙡 𝙛𝙚𝙖𝙩𝙪𝙧𝙚𝙨.
💟 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 𝙄𝙎 𝙈𝘼𝘿𝙀 𝙒𝙄𝙏𝙃 𝙇𝙊𝙑𝙀
𝘼𝙡𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙘𝙖𝙣 𝙗𝙚 𝙪𝙨𝙚𝙙 𝙬𝙞𝙩𝙝 [/](https://telegra.ph/file/e41466544aa55f9cf0d64.jpg)"""

        LOGGER("YukkiMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("YukkiMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("YukkiMusic.plugins" + all_module)
    LOGGER("Yukkimusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
  """𝙃𝙚𝙡𝙡𝙤,
𝙈𝙮 𝙣𝙖𝙢𝙚 𝙞𝙨 🧚 𝙆𝙐𝙏𝙏𝙔 𝘼𝙉𝙂𝙀𝙇 🧚.
𝘼 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙈𝙪𝙨𝙞𝙘+𝙑𝙞𝙙𝙚𝙤 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝙗𝙤𝙩 𝙬𝙞𝙩𝙝 𝙨𝙤𝙢𝙚 𝙪𝙨𝙚𝙛𝙪𝙡 𝙛𝙚𝙖𝙩𝙪𝙧𝙚𝙨.
💟 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 𝙄𝙎 𝙈𝘼𝘿𝙀 𝙒𝙄𝙏𝙃 𝙇𝙊𝙑𝙀
𝘼𝙡𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙘𝙖𝙣 𝙗𝙚 𝙪𝙨𝙚𝙙 𝙬𝙞𝙩𝙝 [/](https://telegra.ph/file/e41466544aa55f9cf0d64.jpg)
𝘼𝙡𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙘𝙖𝙣 𝙗𝙚 𝙪𝙨𝙚𝙙 𝙬𝙞𝙩𝙝 [/](https://telegra.ph/file/e41466544aa55f9cf0d64.jpg)
""".format(
            first_name=name
        ),
        keyboard,
    )
    except NoActiveGroupCall:
        LOGGER("YukkiMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("YukkiMusic").info("Yukki Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("YukkiMusic").info("Stopping Yukki Music Bot! GoodBye")
