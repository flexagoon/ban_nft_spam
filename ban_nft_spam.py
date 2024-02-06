import asyncio
from os import getenv
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message

load_dotenv()

TOKEN = getenv("TOKEN")

dp = Dispatcher()


@dp.message(F.entities)
async def message_handler(message: Message) -> None:
    spam = False
    for entity in message.entities:
        if entity.type == "url":
            url_text = entity.extract_from(message.text)
            if not (url := urlparse(url_text)).scheme:
                url = urlparse("https://" + url_text)
            url = url._replace(path="/encryption.js")
            resp = requests.head(
                url.geturl(),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:122.0) Gecko/20100101 Firefox/122.0"
                },
            )
            if resp.status_code == 200:
                spam = True
                break
    if spam:
        if message.chat.type == "group" or message.chat.type == "supergroup":
            await message.chat.ban(user_id=message.from_user.id)
        await message.delete()


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
