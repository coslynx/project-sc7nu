from datetime import datetime

class TagCooldowns:
    def __init__(self):
        self.cooldowns = {}

    async def add_cooldown(self, user_id, command):
        if user_id in self.cooldowns:
            self.cooldowns[user_id][command] = datetime.now()
        else:
            self.cooldowns[user_id] = {command: datetime.now()}

    async def check_cooldown(self, user_id, command, cooldown_time):
        if user_id in self.cooldowns and command in self.cooldowns[user_id]:
            current_time = datetime.now()
            last_time = self.cooldowns[user_id][command]
            elapsed_time = current_time - last_time
            if elapsed_time.total_seconds() < cooldown_time:
                return False
        return True

    async def clear_cooldowns(self, user_id):
        if user_id in self.cooldowns:
            del self.cooldowns[user_id]