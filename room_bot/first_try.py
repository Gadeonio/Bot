import asyncio
import telegram

import model.my_token


async def main():
    bot = telegram.Bot(model.my_token.get_token())
    async with bot:
        print(await bot.get_me())


async def main2():
    bot = telegram.Bot(model.my_token.get_token())
    async with bot:
        print((await bot.get_updates())[0])


async def main3():
    bot = telegram.Bot(model.my_token.get_token())
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=model.my_token.get_id_chat())

if __name__ == '__main__':
    asyncio.run(main3())