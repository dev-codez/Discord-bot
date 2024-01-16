import discord
from discord.ext import commands
import json
#commands.remove_command('help')

config = json.load(open("config.json"))

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(ignore_extra=False)
    async def help(self, ctx):
        embed=discord.Embed(title="Prefix: >", color=0xdb0606)
        embed.set_author(name="Help commands")
        embed.add_field(name="hire <@member>", value="adds the role given in the config file in both servers", inline=False)
        embed.add_field(name="fire", value="removes all the staff roles and kicks the member from staff server", inline=False)
        await ctx.send(embed=embed)
       
        

def setup(bot):               
    bot.add_cog(help(bot))
