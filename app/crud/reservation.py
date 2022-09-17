# app/crud/reservation.py
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(
            self,
            from_reserve: datetime,
            to_reserve: datetime,
            meetingroom_id: int,
            session: AsyncSession,
    ) -> list[Reservation]:
        return []


reservation_crud = CRUDReservation(Reservation)
