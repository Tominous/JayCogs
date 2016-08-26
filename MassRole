import discord
from discord.ext import commands
import aiohttp
import asyncio

class BetaMassAdd:
	def __init__(self, bot):
		self.bot = bot
		self.discord = __import__('discord')

	@commands.command(pass_context=True)
	async def massrole(self, RankRole):
		await self.bot.say("Adding everyone to role ` " + RankRole + " `, please wait.")
		role = discord.utils.get(ctx.message.server.roles, name=RankRole)
		for RankRole in ctx.message.server.members:
			await self.bot.add_roles(RankRole, role)
		await self.bot.say("Finsihed adding roles.")

def setup(bot):
	bot.add_cog(BetaMassAss(bot))
