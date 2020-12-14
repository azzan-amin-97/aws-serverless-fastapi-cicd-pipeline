from fastapi import FastAPI
from mangum import Mangum

from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

app.include_router(api_router, prefix="/api/v1")


@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)

