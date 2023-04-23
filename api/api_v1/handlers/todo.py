from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID

from schemas.todo_schema import TodoOut

todo_router = APIRouter()

# @todo_router.get('/', summary="Get all todos of the user", response_model=List[TodoOut])
@todo_router.get('/', summary="Get all todos of the user", response_model=None)
async def test():
    pass