from config import OWNER_USERNAME, SUPPORT_GRP
from rudrachat import rudrachat

START = f"""
**๏ ʜᴇʏ, ɪ ᴀᴍ [{rudrachat.name}](t.me/{rudrachat.username})**
**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ**
**──────────────**
**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**
<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ.||</b>
"""

HELP_READ = f"""
<u>**ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {rudrachat.name}**</u>
<u>**ᴀʀᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ!**</u>
**ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ:/**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

TOOLS_DATA_READ = f"""
<u>**ᴛᴏᴏʟs ғᴏʀ {rudrachat.name} ᴀʀᴇ:**</u>
**➻ ᴜsᴇ /repo ғᴏʀ ɢᴇᴛᴛɪɴɢ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ!**
**──────────────**
**➻ ᴜsᴇ /ping ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ᴘɪɴɢ ᴏғ {rudrachat.name}**
**──────────────**
**➻ ᴜsᴇ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴀ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ.**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

CHATBOT_READ = f"""
<u>**ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {rudrachat.name}**</u>
**➻ ᴜsᴇ /chatbot ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**
**๏ ɴᴏᴛᴇ ➻ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴄʜᴀᴛʙᴏᴛ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**
**───────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{rudrachat.name}](https://t.me/{rudrachat.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n**──────────────────**\n**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/RUDRATEAM/RUDRACHATBOT)**\n**──────────────────**\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP}).\n<b>||©️ @{OWNER_USERNAME}||</b>"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{rudrachat.name}](https://t.me/{rudrachat.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{rudrachat.name}](https://t.me/{rudrachat.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{rudrachat.name}](https://t.me/{rudrachat.username})**
"""