from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional
from enum import Enum
import uuid

# Constants
MAX_TITLE_LENGTH = 200
MAX_INGREDIENTS = 50

class Recipe(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str 
    description: str
    ingredients: List[str]
    instructions: List[str]
    tags: List[str] = Field(default_factory=list)
    cuisine: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


    model_config = ConfigDict(
        from_attributes=True
    )


class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    instructions: List[str]
    tags: List[str] = Field(default_factory=list)
    cuisine: str


class RecipeUpdate(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    instructions: List[str]
    tags: List[str]
    cuisine: str
