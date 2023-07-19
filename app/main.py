from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="HotelBooking"
)

@app.get("/api/search/")
def get_hotel():
    return "test"



def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
