from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID

todo_router = APIRouter()

# @todo_router.get('/', summary="Get all todos of the user", response_model=List[TodoOut])
@todo_router.get('/test')
async def test():
    return {"message": "todo router test"}