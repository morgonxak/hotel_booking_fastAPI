from fastapi import FastAPI
from app.booking.router import router as router_booking
import uvicorn

app = FastAPI(
    title="HotelBooking"
)

app.include_router(router_booking)

@app.get("/api/search/")
def get_hotel():
    return "test"



def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
