import asyncio
from load import bot, memory
import aioschedule
from async_manager import*

'''
async def noon():
    return 0


async def schedule():
    aioschedule.every(3).seconds.do(noon)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

 
async def on_startup(dp):
    asyncio.create_task(schedule())
'''    
async def shut_down(dp):
    await bot.close()
    await memory.close()

if __name__ == "__main__":
    from aiogram import executor
    from bot import dp
    #executor.start_polling(dp, on_startup=on_startup, on_shutdown=shut_down)   
    executor.start_polling(dp,  on_shutdown=shut_down)   