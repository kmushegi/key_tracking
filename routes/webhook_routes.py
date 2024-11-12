from fastapi import APIRouter, HTTPException
from models import WebhookEvent
from crud import create_key, update_key, delete_key

router = APIRouter()


@router.post("/")
async def webhook_handler(event: WebhookEvent):
    # TODO: Validate event data
    if event.event_type == "create":
        await create_key(event.data)
    elif event.event_type == "update":
        await update_key(event.data.get("key_id"), event.data)
    elif event.event_type == "delete":
        await delete_key(event.data.get("key_id"))
    else:
        raise HTTPException(status_code=400, detail="Invalid event type")
    return {"message": "Event handled successfully"}
