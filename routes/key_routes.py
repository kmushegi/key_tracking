from fastapi import APIRouter, HTTPException
from models import Key, KeyCreate, KeyUpdate
from crud import create_key, get_all_keys, get_key, update_key, delete_key

router = APIRouter()


@router.post("/", response_model=Key)
async def create_key_endpoint(key: KeyCreate):
    return await create_key(key)


@router.get("/", response_model=list[Key])
async def list_keys():
    return await get_all_keys()


@router.get("/{key_id}", response_model=Key)
async def get_key_endpoint(key_id: str):
    key = await get_key(key_id)
    if key:
        return key
    raise HTTPException(status_code=404, detail="Key not found")


@router.put("/{key_id}", response_model=Key)
async def update_key_endpoint(key_id: str, key_update: KeyUpdate):
    updated_key = await update_key(key_id, key_update.dict())
    if updated_key:
        return updated_key
    raise HTTPException(status_code=404, detail="Key not found")


@router.delete("/{key_id}")
async def delete_key_endpoint(key_id: str):
    result = await delete_key(key_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Key not found")
