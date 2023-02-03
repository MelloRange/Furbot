import discord
from discord.ext import commands

from ..db import db

class Sona(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="save") 
	async def save(self, ctx, *, arg):
		"""
		Saves a text... test function
		"""
		await ctx.send(f'{arg}')
		db.execute('INSERT INTO fursona_characters(user_id, charcter_id, character_name, description) VALUES(?,?,?,?)', ctx.message.author.id, None, None, arg)
		db.commit()
		await ctx.send(f'saved')

	@commands.command(name="get") 
	async def get(self, ctx, char_id:int):
		"""
		gets a text by id
		"""
		text = db.get_one('SELECT description FROM fursona_characters WHERE character_id=?', char_id)
		await ctx.send(f'{text}')


async def setup(bot):
	await bot.add_cog(Sona(bot))