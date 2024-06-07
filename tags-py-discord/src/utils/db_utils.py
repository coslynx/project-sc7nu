import asyncpg
import datetime

class DBUtils:
    def __init__(self, db_pool):
        self.db_pool = db_pool

    async def create_tag_table(self):
        async with self.db_pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute('''
                    CREATE TABLE IF NOT EXISTS tags (
                        tag_id SERIAL PRIMARY KEY,
                        tag_name VARCHAR(255) NOT NULL,
                        tag_content TEXT NOT NULL,
                        created_by BIGINT NOT NULL,
                        created_at TIMESTAMP NOT NULL,
                        category VARCHAR(50),
                        votes INT DEFAULT 0,
                        cooldown BOOLEAN DEFAULT FALSE,
                        suspended BOOLEAN DEFAULT FALSE
                    )
                ''')

    async def add_tag(self, tag_name, tag_content, created_by, category=None):
        async with self.db_pool.acquire() as connection:
            await connection.execute('''
                INSERT INTO tags (tag_name, tag_content, created_by, created_at, category)
                VALUES ($1, $2, $3, $4, $5)
            ''', tag_name, tag_content, created_by, datetime.datetime.now(), category)

    async def remove_tag(self, tag_id):
        async with self.db_pool.acquire() as connection:
            await connection.execute('''
                DELETE FROM tags
                WHERE tag_id = $1
            ''', tag_id)

    async def get_user_tags(self, user_id):
        async with self.db_pool.acquire() as connection:
            return await connection.fetch('''
                SELECT tag_name, tag_content
                FROM tags
                WHERE created_by = $1
            ''', user_id)

    async def get_all_tags(self):
        async with self.db_pool.acquire() as connection:
            return await connection.fetch('''
                SELECT tag_name, tag_content
                FROM tags
            ''')

    async def get_tag_by_name(self, tag_name):
        async with self.db_pool.acquire() as connection:
            return await connection.fetchrow('''
                SELECT tag_content
                FROM tags
                WHERE tag_name = $1
            ''', tag_name)

    async def remove_tag_by_name(self, tag_name):
        async with self.db_pool.acquire() as connection:
            await connection.execute('''
                DELETE FROM tags
                WHERE tag_name = $1
            ''', tag_name)

    async def admin_remove_tag(self, tag_id):
        async with self.db_pool.acquire() as connection:
            await connection.execute('''
                DELETE FROM tags
                WHERE tag_id = $1
            ''', tag_id)

    async def admin_suspend_tag(self, user_id):
        async with self.db_pool.acquire() as connection:
            await connection.execute('''
                UPDATE tags
                SET suspended = TRUE
                WHERE created_by = $1
            ''', user_id)

    async def admin_unsuspend_tag(self, user_id):
        async with self.db_pool.acquire() as connection:
            await connection.execute('''
                UPDATE tags
                SET suspended = FALSE
                WHERE created_by = $1
            ''', user_id)