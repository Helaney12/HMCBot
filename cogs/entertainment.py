import disnake
from disnake import Embed
from disnake.ext import commands

class EntertainmentCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hi(self, inter: disnake.ApplicationCommandInteraction):
        await inter.send('Привет!')

def setup(bot: commands.Bot):
    bot.add_cog(EntertainmentCog(bot))