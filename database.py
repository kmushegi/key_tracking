from motor.motor_asyncio import AsyncIOMotorClient
import os

client = None


def connect_db():
    global client
    client = AsyncIOMotorClient(os.environ.get("MONGO_URL", "0.0.0.0:27017"))


def close_db():
    client.close()


def get_db():
    return client.key_tracking_db
