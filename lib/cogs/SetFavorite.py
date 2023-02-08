import discord
from discord.ext import commands

from ..db import db

class Fave(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="setfave") 
	async def save(self, ctx, char_id: int, new_fave: int):
		"""
		Saves a text... test function
		"""
		#PUT A CHECK HERE TO MAKE SURE THAT THE SONA BELONGS TO THIS USER!!!!!!!!!!!!!!
		db.execute('UPDATE fursona_characters \nSET favorited = ? \nWHERE character_id = ?', new_fave - 1, char_id) # new_fave - 1 because the list starts at 0
		db.commit()
		char_name = db.get_one('SELECT character_name FROM fursona_characters WHERE character_id=?', char_id)
		await ctx.send(f'{char_name} favorite image is now image number {new_fave} from their gallery')


async def setup(bot):
	await bot.add_cog(Fave(bot))