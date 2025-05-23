from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charity_project_active,
                                check_charity_project_exists,
                                check_charity_project_invested,
                                check_charity_project_invested_amount,
                                check_name_duplicate)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.models import Donation
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.investment import process_donation


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Only to superuser. Creates a charitable foundation."""
    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)
    return await process_donation(new_project, Donation, session)


@router.get(
    '/',
    response_model_exclude_none=True,
    response_model=list[CharityProjectDB]
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session)
):
    """Returns a list of all projects."""
    return await charity_project_crud.get_multi(session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Only to superuser. Updates the object of the charity project."""
    charity_project = await check_charity_project_exists(project_id, session)
    charity_project = await check_charity_project_active(charity_project, session)
    if obj_in.name:
        await check_name_duplicate(obj_in.name, session)
    if not obj_in.full_amount:
        return await charity_project_crud.update(charity_project, obj_in, session)
    await check_charity_project_invested_amount(obj_in.full_amount,
                                                charity_project.invested_amount, session)
    return await process_donation(await charity_project_crud.update(
        charity_project, obj_in, session), Donation, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def remove_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """Only to superuser. Deletes the project."""
    charity_project = await check_charity_project_exists(project_id, session)
    await check_charity_project_invested(charity_project, session)
    return await charity_project_crud.remove(charity_project, session)
