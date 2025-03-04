verifyText = "Verify"
emoji = "✅️"
verifiedRoleName = "User"
embedTitle = "Verification"
embedText = "Click the button to get Access to Server"

import os
try:
	import discord
except:
	os.system("pip uninstall discord.py")
	os.system("pip uninstall discord")
	os.system("pip install py-cord")

bot = discord.Bot()

@bot.slash_command()
async def verify(ctx):
    class MyVieww(discord.ui.View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)
        @discord.ui.button(label=verifyText, style=discord.ButtonStyle.grey, emoji=emoji)
        async def bn_callback(self, button, interaction):
            try:
                role = discord.utils.get(ctx.guild.roles, name="User")
                await interaction.user.add_roles(role)
                await interaction.response.send_message("You are verifyed", ephemeral=True)
            except Exception as e:
                await interaction.response.send_message(f"Error\n{e}", ephemeral=True)

    em = discord.Embed(title=embedTitle, description=embedText)
    em.set_footer(text="Coded by dbnw(GitHub)")
    await ctx.send(embed=em, view=MyVieww())
                
bot.run("")