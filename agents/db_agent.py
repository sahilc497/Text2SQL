import logging
from typing import List
from db.factory import DatabaseFactory

logger = logging.getLogger(__name__)

class DBTools:
    @staticmethod
    async def list_databases(db_type: str):
        """Lists all databases for the specified type."""
        try:
            db = await DatabaseFactory.get_db(db_type)
            return await db.list_databases()
        except Exception as e:
            return [f"Error: {str(e)}"]

    @staticmethod
    async def list_tables(db_type: str, db_name: str):
        """Lists all tables in the specified database."""
        try:
            db = await DatabaseFactory.get_db(db_type, db_name)
            return await db.list_tables()
        except Exception as e:
            return [f"Error: {str(e)}"]

from crewai import Agent
from config import settings

class DBAgent:
    def __init__(self):
        self.llm = f"mistral/{settings.MISTRAL_MODEL_FAST}"

    def get_agent(self):
        return Agent(
            role='Database Manager',
            goal='Manage database operations like listing and creating databases, and listing tables.',
            backstory='You are a database administrator. When listing databases or tables, always use a clean Markdown list or table. Be clear and helpful.',
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
