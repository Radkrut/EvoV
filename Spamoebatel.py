# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: spamoebalel
# Description: Спам модуль
# Author: Rodik_God
# Commands:
# .spam | .cspam | .wspam | .delayspam
# ---------------------------------------------------------------------------------


from .. import loader, utils
from asyncio import sleep, gather


def register(cb):
    cb(SpamMod())


class SpamMod(loader.Module):
    """спамоебатель\автор @Rodik_Godmodules"""

    strings = {"name": "Spamoebatel"}

    async def spamcmd(self, message):
        """Обычный спам. Используй .spam -кол-во:{int}- -{текст или ответ на сообщение}- ."""
        try:
            await message.delete()
            args = utils.get_args(message)
            count = int(args[0].strip())
            reply = await message.get_reply_message()
            if reply:
                if reply.media:
                    for _ in range(count):
                        await message.client.send_file(message.to_id, reply.media)
                    return
                else:
                    for _ in range(count):
                        await message.client.send_message(message.to_id, reply)
            else:
                message.message = " ".join(args[1:])
                for _ in range(count):
                    await gather(*[message.respond(message)])
        except:
            return await message.client.send_message(
                message.to_id, ".spam -кол-во:{int}- -{текст или ответ на сообщение}-."
            )

    async def cspamcmd(self, message):
        """Спам любой хуйней. Используй .cspam -{текст или ответ на сообщение}- ."""
        await message.delete()
        reply = await message.get_reply_message()
        if reply:
            msg = reply.text
        else:
            msg = utils.get_args_raw(message)
        msg = msg.replace(" ", "")
        for m in msg:
            await message.respond(m)

    async def wspamcmd(self, message):
        """Спам словами. Используй .wspam -{текст или ответ на сообщение}- ."""
        await message.delete()
        reply = await message.get_reply_message()
        if reply:
            msg = reply.text
        else:
            msg = utils.get_args_raw(message)
        msg = msg.split()
        for m in msg:
            await message.respond(m)

    async def delayspamcmd(self, message):
        """Спам в {мс}  .delayspam -время:{мс}- -кол-во:{шт}- -{текст или ответ на сообщение}-."""
        try:
            await message.delete()
            args = utils.get_args_raw(message)
            reply = await message.get_reply_message() 
            time_ms = int(args.split(" ", 2)[0])
            count = int(args.split(" ", 2)[1])
            if reply:
                if reply.media:
                    for _ in range(count):
                        await message.client.send_file(
                            message.to_id, reply.media, reply_to=reply.id
                        )
                        await sleep(time_ms/1000)
                else:
                    for _ in range(count):
                        await reply.reply(args.split(" ", 2)[2])
                        await sleep(time_ms/1000)
            else:
                spammsg = args.split(" ", 2)[2]
                for _ in range(count):
                    await message.respond(spammsg)
                    await sleep(time_ms/1000)
        except:
            return await message.client.send_message(
                message.to_id, ".delayspam -время:{int}- -кол-во:{int}- -{текст или ответ на сообщение}-"
            )