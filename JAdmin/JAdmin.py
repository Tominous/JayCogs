import discord
from discord.ext import commands
import asyncio
import time
from __main__ import send_cmd_help
import datetime
from .utils import checks

class JAdmin:
    """Simple admin commands."""

    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def binfo(self,ctx):
        """Basic stats about the bot and server"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        up = abs(self.bot.uptime - int(time.perf_counter()))
        up = str(datetime.timedelta(seconds=up))
        await self.bot.say("***Calculating...***")
        await self.bot.say("``**Ping:** ``{}ms``\n**Up Time:** ``{}``\n**Members:** ``{}``\n**Roles:** ``{}``\n**Channels:** ``{}``".format(round((t2-t1)*1000), up, len(ctx.message.server.members), len(ctx.message.server.roles), len(ctx.message.server.channels)))

    @commands.group(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(administrator=True)
    async def promote(self, ctx, role, user : discord.Member):
        current = ctx.message.server.roles
        role = discord.utils.get(current, name=role)
        await self.bot.add_roles(user, role)
        await self.bot.say("Added role ``{}`` to {}!".format(role, user))


def setup(bot):
    bot.add_cog(JAdmin(bot))
