from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"

class Message(BaseModel):
    role: Role
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[list[Message]] = None
    
class ChatResponse (BaseModel):
    response: str
    source:  Optional[list[str]] = None