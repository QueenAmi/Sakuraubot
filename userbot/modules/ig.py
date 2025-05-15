import re
import requests
import asyncio 
import random

from pyrogram import filters
from userbot import *
from pyrogram.types import Message


@CB.UBOT("reel")
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            f"Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ Iɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ URL ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ"
        )
        return
    url = message.text.split()[1]
    if not re.match(
        re.compile(r"^(https?://)?(www\.)?(instagram\.com|instagr\.am)/.*$"), url
    ):
        return await message.reply_text(
            f"Tʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ URL ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ Iɴsᴛᴀɢʀᴀᴍ URL"
        )
    a = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    api_url = f"https://insta-dl.hazex.workers.dev/?url={url}"

    response = requests.get(api_url)
    try:
        result = response.json()
        data = result["result"]
    except Exception as e:
        f = f"Eʀʀᴏʀ :\n{e}"
        try:
            await a.edit(f)
        except Exception:
            await message.reply_text(f)
            return await app.send_message(LOG_GROUP_ID, f)
        return await app.send_message(LOG_GROUP_ID, f)
    if not result["error"]:
        video_url = data["url"]
        duration = data["duration"]
        quality = data["quality"]
        type = data["extension"]
        size = data["formattedSize"]
        caption = f"<blockquote><b>**ɴɪ ʜᴀsɪʟɴʏᴀ ᴊɪɴɢ.**\n\n▢ **Dᴜʀᴀᴛɪᴏɴ :** {duration}\n├ **Qᴜᴀʟɪᴛʏ :** {quality}\n├ **Tʏᴘᴇ :** {type}\n╰ **Sɪᴢᴇ :** {size}\n\n➻ **ᴄʀᴇᴀᴛᴇᴅ ʙʏ :** {bot.me.mention}<b></blockquote>"
        await a.delete()
        await message.reply_video(video_url, caption=caption)
    else:
        try:
            return await a.edit(f"<u>Fᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʀᴇᴇʟ</u>")
        except Exception:
            return await message.reply_text(f"<u>Fᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʀᴇᴇʟ</u>")


__MODULE__ = "ʀᴇᴇʟ"
__HELP__ = """
<blockquote><b>**ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ:**
• `/reel [URL]`: ᴅᴏᴡɴʟᴏᴀᴅ ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟs. Pʀᴏᴠɪᴅᴇ ᴛʜᴇ ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ URL ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.<b></blockquote>
"""
