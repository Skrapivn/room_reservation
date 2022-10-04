# Понадобится для того, чтобы задать временные интервалы
from datetime import datetime
# Класс «обёртки»
from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser

from app.crud.reservation import reservation_crud
from app.services.google_api import (set_user_permissions, spreadsheets_create,
                                     spreadsheets_update_value)
# Создаём экземпляр класса APIRouter
router = APIRouter()


@router.post(
    '/',
    # Тип возвращаемого эндпоинтом ответа
    response_model=list[dict[str, int]],
    # Определяем зависимости
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        # Начало периода
        from_reserve: datetime,
        # Конец периода
        to_reserve: datetime,
        # Сессия
        session: AsyncSession = Depends(get_async_session),
        # «Обёртка»
        wrapper_services: Aiogoogle = Depends(get_service)
):
    """Только для суперюзеров. \n
    Формирование отчёта в гугл-таблице с количеством бронирований
     каждой переговорки за указанный период."""
    reservations = await reservation_crud.get_count_res_at_the_same_time(
        from_reserve, to_reserve, session
    )
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    reservations,
                                    wrapper_services)
    return reservations
