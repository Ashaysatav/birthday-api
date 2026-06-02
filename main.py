from fastapi import FastAPI, Query
from datetime import date

app = FastAPI(title="Birthday API", description="Is today your birthday?")


@app.get("/birthday")
def check_birthday(
    month: int = Query(..., ge=1, le=12, description="Birth month (1-12)"),
    day: int = Query(..., ge=1, le=31, description="Birth day (1-31)"),
):
    today = date.today()
    if today.month == month and today.day == day:
        return {"birthday": True, "message": "Hey happy birthday! 🎂"}
    return {"birthday": False, "message": "No, not today, MF."}


@app.get("/")
def root():
    return {"message": "Birthday API is live. Try /birthday?month=6&day=2"}
