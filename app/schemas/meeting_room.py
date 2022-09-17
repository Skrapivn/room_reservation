from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(
    ..., min_length=1, max_length=100,
    title='Название переговорки', description='Укажите название переговорной комнаты'
    )

    class Config:
        @validator('name')
        def max_lenght(cls, value: str):
            if len(value) > 100:
                raise ValueError('Название не должно превышать 100 символов')
            if value.isnumeric():
                raise ValueError('Название не может быть числом')
            if value is None:
                raise ValueError('Название не может быть пустым')
            return value


class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value       


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
