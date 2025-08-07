from fastapi import APIRouter


router = APIRouter(
    prefix="",
    tags=['Auth & Пользователи']
)



@router.get('/auth/')
async def get_user():
    return {'user': 'authenticated'}