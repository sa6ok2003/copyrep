from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 494588959
id_channel = -1001132571120

id_class = -1001253317345


@app.on_message()
async def payments (client,message):
    if message.chat.id == id_channel:
        await app.copy_message(message_id=message.message_id, chat_id=id_class,from_chat_id=id_class)


app.run()