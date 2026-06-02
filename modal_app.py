import modal

app = modal.App("birthday-api")

image = modal.Image.debian_slim().pip_install("fastapi")


@app.function(image=image)
@modal.asgi_app()
def serve():
    from fastapi import FastAPI, Query
    from datetime import date

    fastapi_app = FastAPI(title="Birthday API")

    @fastapi_app.get("/birthday")
    def check_birthday(
        month: int = Query(..., ge=1, le=12),
        day: int = Query(..., ge=1, le=31),
    ):
        today = date.today()
        if today.month == month and today.day == day:
            return {"birthday": True, "message": "Hey happy birthday! 🎂"}
        return {"birthday": False, "message": "No, not today, MF."}

    @fastapi_app.get("/")
    def root():
        return {"message": "Birthday API is live. Try /birthday?month=6&day=2"}

    return fastapi_app
