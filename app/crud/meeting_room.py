# app/crud/meeting_room.py
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.meeting_room import MeetingRoom


class CRUDMeetingRoom(CRUDBase):

    async def get_room_id_by_name(
            self,
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(MeetingRoom.id).where(
                MeetingRoom.name == room_name
            )
        )
        return db_room_id.scalars().first()


meeting_room_crud = CRUDMeetingRoom(MeetingRoom)
