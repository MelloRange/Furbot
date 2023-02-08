import discord
from discord.ext import commands

from ..db import db

class AddPic(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="addpic") 
	async def addpic(self, ctx, char_id, pic_url):
		"""
		Saves a text... test function
		"""
		db.execute('INSERT INTO character_art(character_id, art_image, description) VALUES(?,?,?)', char_id, pic_url, None)
		db.commit()
		char_name = db.get_one('SELECT character_name FROM fursona_characters WHERE character_id=?', char_id)
		await ctx.send(f"Art added to {char_name}'s gallery")

async def setup(bot):
	await bot.add_cog(AddPic(bot))