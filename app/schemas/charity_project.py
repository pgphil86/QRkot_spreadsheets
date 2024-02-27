from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt


class CharityProjectBase(BaseModel):
    """The basic scheme of the project."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    """Schema for creating a new project."""
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    """Schema for updating the project."""

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectBase):
    """Schema for displaying projects."""
    id: int
    invested_amount: Optional[int]
    create_date: Optional[datetime]
    close_date: Optional[datetime]
    fully_invested: Optional[bool]

    class Config:
        orm_mode = True
