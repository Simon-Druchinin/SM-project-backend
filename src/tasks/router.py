from fastapi import APIRouter, Depends

from src.auth.config import current_user
from src.tasks.tasks import send_email_report


router = APIRouter(
    prefix="/report",
    tags=["celery tasks"]
)

@router.get("/test-email")
async def get_test_email(user=Depends(current_user)):
    send_email_report.delay(user.username)
    return {
        "status": 200,
        "data": "The Letter was sent",
        "details": None
    }