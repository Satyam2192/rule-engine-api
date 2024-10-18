from motor.motor_asyncio import AsyncIOMotorClient

client = None

async def init_db():
    global client
    client = AsyncIOMotorClient('mongodb://localhost:27017/')

async def close_db():
    global client
    if client:
        client.close()