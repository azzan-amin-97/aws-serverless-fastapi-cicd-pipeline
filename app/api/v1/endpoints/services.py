from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def testing_child_resource():
    return {"message": "Hi There! This is my route endpoint."}