from fastapi import FastAPI
import decouple
import uvicorn

from router import router

def main():
    app = FastAPI()

    port = int(decouple.config("PORT", 8000))
    host = "0.0.0.0"

    app.include_router(router)

    uvicorn.run(
        app = app,
        port = port,
        host = host
    )

if __name__ == "__main__":
    main()