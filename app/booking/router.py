from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)

@router.get("")
def get_bookings():
    return "hello"


@router.get("/temp")
def get_bookings1():
    return "hello"