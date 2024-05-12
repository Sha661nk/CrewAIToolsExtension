import json
import redis
import sqlalchemy
from crewai_tools import BaseTool
from pymongo import MongoClient

# Tool for loading data to relational databases like MySQL, SQLite, PostgreSQL
class SQLDatabaseWriteTool(BaseTool):
    def __init__(self, db_url):
        self.engine = sqlalchemy.create_engine(db_url)
    
    def _run(self, table_name, data):
        with self.engine.connect() as connection:
            connection.execute(
                sqlalchemy.text(f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES ({':'+', :'.join(data.keys())})"),
                **data
            )
        return "Data inserted successfully in SQL database."

# Tool for loading data to MongoDB
class MongoDBWriteTool(BaseTool):
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
    
    def _run(self, data):
        self.collection.insert_one(data)
        return "Data inserted successfully in MongoDB."

# Tool for loading data to Redis
class RedisWriteTool(BaseTool):
    def __init__(self, host, port, password):
        self.redis_client = redis.Redis(host=host, port=port, password=password, decode_responses=True)
    
    def _run(self, key, value):
        self.redis_client.set(key, json.dumps(value))
        return "Data inserted successfully in Redis."

# Example
sql_tool = SQLDatabaseWriteTool('---Input SQL Hosted url---')
mongo_tool = MongoDBWriteTool('---Input SQL Hosted url---', '---Input DB Name---', '---Input Collection---')
redis_tool = RedisWriteTool('---Input Host---', "---Input Port---", None)

# Insert data
sql_result = sql_tool.run('table', {'column1': 'value1', 'column2': 'value2'})
mongo_result = mongo_tool.run({'name': 'Sash G', 'age': 28})
redis_result = redis_tool.run('user_id:1000', {'name': 'Sash G', 'age': 28})

print(sql_result)
print(mongo_result)
print(redis_result)