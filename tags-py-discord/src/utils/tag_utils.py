import discord
import asyncpg

class TagUtils:
    def __init__(self, bot):
        self.bot = bot

    async def add_tag(self, tag_name, tag_content, user_id):
        # Add tag to the database
        pass

    async def remove_tag(self, tag_name, user_id):
        # Remove tag from the database
        pass

    async def get_user_tags(self, user_id):
        # Get all tags created by the user
        pass

    async def get_all_tags(self):
        # Get all tags available in the server
        pass

    async def get_tag_content(self, tag_name):
        # Get the content of a specific tag
        pass

    async def remove_admin_tag(self, tag_name):
        # Remove any tag in the server as an admin
        pass

    async def suspend_user_tag(self, user_id):
        # Suspend a user from using add-tag and remove-tag commands
        pass

    async def unsuspend_user_tag(self, user_id):
        # Unsuspend a user from using add-tag and remove-tag commands
        pass

    async def get_tag_categories(self):
        # Get all tag categories
        pass

    async def search_tags(self, query):
        # Search for tags based on a query
        pass

    async def vote_tag(self, tag_name, user_id):
        # Vote for a specific tag
        pass

    async def add_tag_cooldown(self, user_id):
        # Add a cooldown for tag commands for a user
        pass

    async def check_tag_permission(self, user_id, required_role):
        # Check if a user has permission to use tag commands based on role
        pass

    async def get_tag_history(self, tag_name):
        # Get the history of changes made to a tag
        pass

    async def send_tag_notification(self, user_id, tag_name, notification_type):
        # Send a notification to a user for a new tag added or removed
        pass

    async def update_tag(self, tag_name, tag_content, user_id):
        # Update the content of a tag
        pass