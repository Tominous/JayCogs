import discord
from discord.ext import commands
import asyncio
import time
from __main__ import send_cmd_help
import datetime

class JAdmin:
    """Simple admin commands."""

    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def serverstats(self,ctx):
        """Shows basic stats for about the bot and server"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        up = abs(self.bot.uptime - int(time.perf_counter()))
        up = str(datetime.timedelta(seconds=up))
        await self.bot.say("***Calculating...***")
        await self.bot.say("``**Ping:** ``{}ms``\n**Up Time:** ``{}``\n**Members:** ``{}``\n**Roles:** ``{}``\n**Channels:** ``{}``".format(round((t2-t1)*1000), up, len(ctx.message.server.members), len(ctx.message.server.roles), len(ctx.message.server.channels)))


def setup(bot):
    bot.add_cog(JAdmin(bot))
