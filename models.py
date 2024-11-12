from pydantic import BaseModel, Field
from typing import Literal, Optional


class Key(BaseModel):
    key_id: str
    key_type: Literal["Guest", "Cleaners", "Maintenance"]  # TODO: use enum
    status: Literal["Available", "In Use"]  # TODO: use enum
    current_user: Optional[str] = None


class KeyUpdate(BaseModel):
    status: Literal["Available", "In Use"]  # TODO: use enum
    current_user: Optional[str]


class KeyCreate(Key):
    pass


class WebhookEvent(BaseModel):
    event_type: Literal["create", "update", "delete"]
    data: dict
