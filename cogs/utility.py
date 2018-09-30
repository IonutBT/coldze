import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep


class Utility():
	def __init__(self, bot):
		self.bot = bot
		colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]











	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def support(self, ctx):
		'Returns the link to the support server'
		em = discord.Embed(title="", description="", color=discord.Colour.blue())
		em.add_field(name='Support Server', value='[Here]( https://discord.gg/xeGn4A )')
		await ctx.send(embed=em)

	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def emoji(self, ctx, emoji: discord.Emoji):
		'''Shows info about an Emoji
		Works only for custom ones
		------------------------
		Ex:
		cz?emoji :emoji:'''
		await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}')


	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases= ["sinfo"])
	async def serverinfo(self, ctx):
		"""Get the server info"""
		em = discord.Embed(color=discord.Colour.blue())
		em.add_field(name=':paintbrush: Name', value=f'{ctx.author.guild.name}', inline=False)
		em.add_field(name=':crown: Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=False)
		em.add_field(name=':mountain_snow: Icon', value='Do cz?servericon', inline=False)
		em.add_field(name=':family_mwgb: Roles', value='Do cz?serverroles', inline=False)
		em.add_field(name=':bust_in_silhouette: Members', value=f'{ctx.guild.member_count}', inline=False)
		em.add_field(name=':clock1: Created at', value=ctx.guild.created_at, inline=False)
		em.set_thumbnail(url=ctx.guild.icon_url)
		await ctx.send(embed=em)



	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases=['sroles'])
	async def serverroles(self, ctx):
		"""Get the server roles"""
		em = discord.Embed(color=discord.Colour.blue())
		em.add_field(name=f'Server Roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for g in ctx.guild.roles))
		await ctx.send(embed=em)



	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def avatar(self, ctx, member: discord.Member=None):
		"""Get a member's avatar
		-------------------
		Ex:
		cz?avatar @Adytzu"""
		if member is None:
			member = ctx.author
		em = discord.Embed(title="", color=discord.Colour.blue())
		em.set_author(name=f"{member}'s avatar")
		em.set_image(url=member.avatar_url)
		msg = await ctx.send(embed=em)




	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases =['sicon'])
	async def servericon(self, ctx):
		'Get the server icon'
		em = discord.Embed(title="", color=discord.Colour.blue())
		em.set_author(name=f"{ctx.guild.name}'s icon")
		em.set_image(url=ctx.guild.icon_url)
		await ctx.send(embed=em)





	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases= ["pinfo"])
	async def playerinfo(self, ctx, member: discord.Member=None):
		"""Get a member's info
		-------------------
		Ex:
		cz?playerinfo @Adytzu"""
		if member is None:
			member = ctx.author
		em = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
		em.set_author(name="Player info")
		em.add_field(name="Name", value=member.name)
		em.add_field(name="ID", value=member.id)
		em.add_field(name="BOT:", value=member.bot)
		em.add_field(name="Tag", value=member.discriminator)
		em.add_field(name="Top Role", value=member.top_role)
		em.add_field(name="Nick", value=member.nick)
		em.add_field(name="Joined", value=member.joined_at)
		em.set_thumbnail(url=member.avatar_url)
		msg = await ctx.send(embed=em)
















































def setup(bot):
        bot.add_cog(Utility(bot))
