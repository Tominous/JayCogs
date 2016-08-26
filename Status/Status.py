import discord
from discord.ext import commands
import time
from __main__ import send_cmd_help
import datetime
import asyncio


class JStatus:
    """Status"""

    def __init__(self,bot):
        self.bot = bot
        

    @commands.command(pass_context=True)
    async def status(self,ctx):
        """Shows basic stats for about the bot and server"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        up = abs(self.bot.uptime - int(time.perf_counter()))
        up = str(datetime.timedelta(seconds=up))
        await self.bot.say("**Calculating**\n")
        await self.bot.say("***Ping:*** ``{}``ms".format(round((t2-t1)*1000)))
        await self.bot.say("\n***Uptime:*** ``{}``".format(up))
        await self.bot.say("***Members:*** ``{}``".format(len(ctx.message.server.members)))


def setup(bot):
    bot.add_cog(JStatus(bot))
