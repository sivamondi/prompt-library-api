from typing import Dict, Any
from pydantic import BaseModel

class PromptCreate(BaseModel):
    name: str
    content: Dict[str, Any]

class PromptResponse(BaseModel):
    name: str
    content: Dict[str, Any] 