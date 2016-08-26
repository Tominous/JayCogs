import discord
from discord.ext import commands
import asyncio

class JCounter:
    """Displays how many channels and roles are in a server."""
    def __init__(self, bot):
        self.bot = bot
#Original Code by Discordian. Remade Majorly by Jay

    @commands.command(pass_context=True, no_pm=True)
    async def counter(self, ctx):
        """Displays how many channels and roles are in a server."""
        await self.bot.say("***Calculating***")
        await self.bot.say("**Roles:** {}".format(len(ctx.message.server.roles)))
        await self.bot.say("**Channels:** {}".format(len(ctx.message.server.channels)))

def setup(bot):
    bot.add_cog(JCounter(bot))
