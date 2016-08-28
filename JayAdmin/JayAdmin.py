import discord
from discord.ext import commands
import asyncio
import time
import datetime
from .utils import checks

class JAdmin:
    """Simple admin commands."""

    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True, no_pm=True)
    async def binfo(self,ctx):
        """Basic stats about the bot and server"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        up = abs(self.bot.uptime - int(time.perf_counter()))
        up = str(datetime.timedelta(seconds=up))
        await self.bot.say("***Calculating...***")
        await asyncio.sleep(2)
        await self.bot.say("**Ping:** ``{}ms``\n**Up Time:** ``{}``\n**Members:** ``{}``\n**Roles:** ``{}``\n**Channels:** ``{}``".format(round((t2-t1)*1000), up, len(ctx.message.server.members), len(ctx.message.server.roles), len(ctx.message.server.channels)))

    @commands.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(administrator=True)
    async def promote(self, ctx, role: discord.Role, user: discord.Member):
        """Gives a role to a user"""
        await self.bot.add_roles(user, role)
        await self.bot.say("I added ``{}`` to {}!".format(role, user))
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(administrator=True)
    async def demote(self, ctx, role: discord.Role, user: discord.Member):
        """Removes a role from a user"""
        await self.bot.remove_roles(user, role)
        await self.bot.say("I removed ``{}`` from {}!".format(role, user))
        
    #Thanks to Discordian for the help with MassPromote/MassDemote
    
    @commands.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permission(administrator=True)
    async def masspromote(self, ctx, role: discord.Role):
        """Mass promotes everyone in the server."""
        await self.bot.say("I am currently starting to add everyone to ``{}``".format(role))
        roletoadd = discord.utils.get(ctx.message.server.role, name=role)
        for member in ctx.message.server.members:
            await self.bot.add_roles(member, roletoadd)
        await self.bot.say("Added role ``{}`` to everyone.".format(role)
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permission(administrator=True)
    async def massdemote(self, ctx, role: discord.Role):
        """Mass promotes everyone in the server."""
        await self.bot.say("I am currently starting to add everyone to ``{}``".format(role))
        roletoadd = discord.utils.get(ctx.message.server.role, name=role)
        for member in ctx.message.server.members:
            await self.bot.remove_roles(member, roletoadd)
        await self.bot.say("Added role ``{}`` to everyone.".format(role)
    



def setup(bot):
    bot.add_cog(JAdmin(bot))
