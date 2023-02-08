import typing
import discord
from discord.ext import commands
from discord.ui import Button, View

from ..db import db

class Gallery(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="gallery") 
	async def Gallery(self, ctx: commands.Context, char_id):
		"""
		Makes an image gallery that users can flip through
		"""
		
		# ------------------------- CREATING VARIABLES -------------------------
		
		char_name = db.get_one('SELECT character_name FROM fursona_characters WHERE character_id=?', char_id)
		char_description = db.get_one('SELECT description FROM fursona_characters WHERE character_id=?', char_id)
		favorited = db.get_one('SELECT favorited FROM fursona_characters WHERE character_id=?', char_id)
		
		# Temporary image list, images will be taken from the database once it's set up
		# These could maybe be arrays/tuples of strings later? With a URL, a description and tags
		# It'd maybe be like ["url goes here", "description", "tag1,tag2,tag3,tag4..."]
		image_list = []
		cursor = db.get_column('SELECT art_image FROM character_art WHERE character_id=?',char_id)
		for row in cursor:
			image_list.append(row)
		current_position = favorited
		view = View()
		
		#This is the embed that'll contain the images, it'll be edited whenever a new image is requested
		gallery_embed = discord.Embed(
			title = f"{char_name}'s gallery",
			description = f"Viewing image {current_position + 1}/{len(image_list)}")
		
		gallery_embed.add_field(
            name = "Description:",
            value = f"{char_description}",
            inline = False);
		
		
		# ------------------------- BUTTON STUFF -------------------------
		
		left_button = Button(label="Left Button", style=discord.ButtonStyle.green, emoji='⬅️')
		right_button = Button(label="Right Button", style=discord.ButtonStyle.green, emoji='➡️')
		
		# I feel like there's a better way to do this, but we haven't used python in a while so we're not sure
		async def left_callback(interaction):
			nonlocal current_position
			nonlocal gallery_embed
			nonlocal image_list
			
			current_position -= 1
			if current_position < 0: # Loop if the front of the gallery is hit
				current_position = len(image_list) - 1
			gallery_embed.set_image(url = image_list[current_position])
			gallery_embed.description = f"Viewing image {current_position + 1}/{len(image_list)}"
			await interaction.response.edit_message(content=f'Better embed gallery test', embed = gallery_embed, view=view) # Not sure if it has to be edited or it just needs an "await"
			

		async def right_callback(interaction):
			nonlocal current_position
			nonlocal gallery_embed
			nonlocal image_list
			
			current_position += 1
			if current_position >= len(image_list): # Loop if the back of the gallery is hit
				current_position = 0
			
			gallery_embed.set_image(url = image_list[current_position])
			gallery_embed.description = f"Viewing image {current_position + 1}/{len(image_list)}" 
			await interaction.response.edit_message(content=f'Better embed gallery test', embed = gallery_embed, view=view) # Not sure if it has to be edited or it just needs an "await"
			
		
		left_button.callback = left_callback
		right_button.callback = right_callback
		
		# ------------------------- END OF BUTTON STUFF -------------------------
		
		
		view.add_item(left_button)
		view.add_item(right_button)
		
		gallery_embed.set_image(url = image_list[current_position])
		await ctx.send(f'Image gallery!', embed = gallery_embed, view=view)

async def setup(bot):
	await bot.add_cog(Gallery(bot))