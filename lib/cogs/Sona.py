import discord
from discord.ext import commands

from ..db import db

class Sona(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="save") 
	async def save(self, ctx, char_name, char_description):
		"""
		Saves a text... test function
		"""
		char_id = db.get_one('INSERT INTO fursona_characters(user_id, character_name, description) VALUES(?,?,?) RETURNING character_id', ctx.message.author.id, char_name, char_description)
		db.commit()
		await ctx.send(f'{char_name} has been saved with id {char_id}')

	@commands.command(name="get") 
	async def get(self, ctx, char_id:int):
		"""
		gets a text by id
		"""
		name = db.get_one('SELECT character_name FROM fursona_characters WHERE character_id=?', char_id)
		description = db.get_one('SELECT description FROM fursona_characters WHERE character_id=?', char_id)
		await ctx.send(f'{name}: {description} (sona id {char_id})')


async def setup(bot):
	await bot.add_cog(Sona(bot))