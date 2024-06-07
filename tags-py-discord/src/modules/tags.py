import discord
from discord.ext import commands

class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add-tag')
    async def add_tag(self, ctx, tag_name, tag_content):
        pass

    @commands.command(name='remove-tag')
    async def remove_tag(self, ctx, tag_name):
        pass

    @commands.command(name='mytag')
    async def my_tag(self, ctx):
        pass

    @commands.command(name='show-all-tags')
    async def show_all_tags(self, ctx):
        pass

    @commands.command(name='tag-open')
    async def tag_open(self, ctx, tag_name):
        pass

    @commands.command(name='admin-remove-tag')
    @commands.has_permissions(administrator=True)
    async def admin_remove_tag(self, ctx, tag_name):
        pass

    @commands.command(name='admin-suspend-tag')
    @commands.has_permissions(administrator=True)
    async def admin_suspend_tag(self, ctx, user: discord.Member):
        pass

    @commands.command(name='admin-unsuspend-tag')
    @commands.has_permissions(administrator=True)
    async def admin_unsuspend_tag(self, ctx, user: discord.Member):
        pass

def setup(bot):
    bot.add_cog(Tags(bot))