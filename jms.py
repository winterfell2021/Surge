from pagermaid import bot, scheduler
from pagermaid.listener import listener
from pagermaid.utils import alias_command
from telethon import events
from asyncio import TimeoutError
bot_name = 'qweybgbot'
@listener(outgoing=True, command=alias_command("jms"),
          description="卷毛鼠签到")
async def jmssign(context):
    try:
        await bot.send_message(bot_name, '/checkin')
        await context.edit('签到中')
        text = "已签到"
        async for message in bot.iter_messages(bot_name):
            if "签到前" in message.message:
                x, op, y = message.message.split('\n')[1].split(' ')[:3]
                ans = -1
                x = int(x)
                y = int(y)
                if op == '乘以':
                    ans = x * y
                elif op == '加上':
                    ans = x + y
                elif op == '除以':
                    ans = x // y
                else:
                    ans = x - y
                result = await message.click(text=str(ans))
                text = "卷毛鼠签到结果：\n" + result.message
            else:
                text = "卷毛鼠签到结果：已签到"
            break
        await context.edit(text)
    except:
        await context.edit("卷毛鼠签到失败，请检查！")
        
@scheduler.scheduled_job("cron", hour="10", id="jmssign")
async def jmsautosign():
    try:
        await bot.send_message(bot_name, '/checkin')
        text = "已签到"
        async for message in bot.iter_messages(bot_name):
            if "签到前" in message.message:
                x, op, y = message.message.split('\n')[1].split(' ')[:3]
                ans = -1
                x = int(x)
                y = int(y)
                if op == '乘以':
                    ans = x * y
                elif op == '加上':
                    ans = x + y
                elif op == '除以':
                    ans = x // y
                else:
                    ans = x - y
                result = await message.click(text=str(ans))
                text = "卷毛鼠签到结果：\n" + result.message
            else:
                text = "卷毛鼠签到结果：已签到"
            break
        await bot.send_message('me', text)
    except:
        await bot.send_message('me', "卷毛鼠签到失败，请检查！")
