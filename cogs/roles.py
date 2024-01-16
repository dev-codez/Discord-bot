'''
the first server id in the config file is the main server and the second one is the staff
the roles in the config file are the roles added to the person when using the hire command
'''



import discord
import discord.guild
from discord.ext import commands
import discord.member
import json

config = json.load(open("config.json"))


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def hire(self, ctx, member : discord.Member = None):
        if member == None:
            return await ctx.send("run this command again but next time actually mention someone to hire")

        for guild_id in config["servers"]:
            guild = self.bot.get_guild(guild_id)
            
            role = discord.utils.get(guild.roles, name="Staff")

            member = guild.get_member(member.id)
            await member.add_roles(role)
            await ctx.send(f"Added {role} role to {member.mention} in {guild}")



    


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def fire(self, ctx, member : discord.Member=None, action="kick", *, reason=None):
        if member == None:
            return await ctx.send("run this command again but next time actually mention someone to fire")
        

        guild_main = self.bot.get_guild(config["servers"][0])
        member = guild_main.get_member(member.id)
        for i in config["roles"]:
            role = discord.utils.get(guild_main.roles, name=i)
            await member.remove_roles(role) 
        await ctx.send("Removed all the staff roles from the main server")

        guild_staff = self.bot.get_guild(config["servers"][1])
        member = guild_staff.get_member(member.id)  
        try:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member.mention} from the staff server")
        except:
            await ctx.send(f"there was a problem kicking {member.mention} from the Staff server")






    @hire.error
    @fire.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have the permission to do that")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("I don't think a member exists by that name")
        elif isinstance(error, discord.Forbidden):
            await ctx.send("My role is lower then the person you are trying to fire")
        elif isinstance(error, discord.HTTPException):
            await ctx.send("An error occured. Please try again")
        elif isinstance(error, commands.CommandNotFound):
            return
        

def setup(bot):               
    bot.add_cog(Roles(bot))
