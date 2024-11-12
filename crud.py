from models import Key
from database import get_db
from fastapi import HTTPException


async def create_key(key: Key):
    db = get_db()
    existing_key = await db.keys.find_one({"key_id": key.key_id})
    if existing_key:
        raise HTTPException(status_code=409, detail="Key ID already exists")
    return await db.keys.insert_one(key.dict())


async def get_all_keys():
    db = get_db()
    keys = await db.keys.find().to_list(100)
    return keys


async def get_key(key_id: str):
    db = get_db()
    return await db.keys.find_one({"key_id": key_id})


async def update_key(key_id: str, key_update: dict):
    db = get_db()
    await db.keys.update_one({"key_id": key_id}, {"$set": key_update})
    return await get_key(key_id)


async def delete_key(key_id: str):
    db = get_db()
    await db.keys.delete_one({"key_id": key_id})
    return {"message": "Key deleted"}
