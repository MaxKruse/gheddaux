from discord.ext import commands

from singletons.bot import Bot


class Welcome(commands.Cog):
	@commands.Cog.listener()
	async def on_member_join(self, member):
		await Bot().welcome_channel_id.send(f"Welcome to Ripple, {member.mention}!.")
