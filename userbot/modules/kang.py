from userbot import *

__MODULE__ = "ᴋᴀɴɢ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀɴɢ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}kang</code> [ʀᴇᴘʟʏ ᴛᴏ ɪᴍᴀɢᴇ/sᴛɪᴄᴋᴇʀ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴅᴀɴ ᴄᴏsᴛᴜᴍ ᴇᴍᴏᴊɪ sᴛɪᴄᴋᴇʀ ᴋᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ

  <b>➢ ɴᴏᴛᴇ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴘᴀᴋᴇᴛ ꜱᴛɪᴋᴇʀ ʙᴀʀᴜ ɢᴜɴᴀᴋᴀɴ ᴀɴɢᴋᴀ ᴅɪ ʙᴇʟᴀᴋᴀɴɢ !ᴋᴀɴɢ.
  <b>➢ ᴇxᴀᴍᴘʟᴇ:</b> <code>kang 2</code> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴅᴀɴ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴇ ᴘᴀᴋᴇᴛ ꜱᴛɪᴋᴇʀ ᴋᴇ-𝟸<b></blockquote>
"""

@CB.UBOT("kang")
async def _(client, message):
    await kang_cmd(client, message)
