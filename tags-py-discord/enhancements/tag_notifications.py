import discord

class TagNotifications:
    def __init__(self, client):
        self.client = client

    async def notify_tag_added(self, tag_name, user):
        notification_message = f"Tag '{tag_name}' has been added by {user.display_name}"
        await user.send(notification_message)

    async def notify_tag_removed(self, tag_name, user):
        notification_message = f"Tag '{tag_name}' has been removed by {user.display_name}"
        await user.send(notification_message)

    async def notify_tag_voted(self, tag_name, user):
        notification_message = f"Tag '{tag_name}' has been upvoted by {user.display_name}"
        await user.send(notification_message)

    async def notify_tag_cooldown(self, user):
        notification_message = "You are on tag command cooldown. Please wait before using tag commands again."
        await user.send(notification_message)

    async def notify_tag_permission_denied(self, user):
        notification_message = "You do not have permission to use this tag command."
        await user.send(notification_message)