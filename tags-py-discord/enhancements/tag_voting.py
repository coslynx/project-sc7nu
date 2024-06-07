import discord
from discord.ext import commands

class TagVoting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vote-tag', help='Vote for a specific tag.')
    async def vote_tag(self, ctx, tag_name: str):
        # Logic to handle tag voting
        pass

    @commands.command(name='top-tags', help='Display the top voted tags.')
    async def top_tags(self, ctx):
        # Logic to display top voted tags
        pass

def setup(bot):
    bot.add_cog(TagVoting(bot))