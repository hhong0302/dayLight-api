from typing import Annotated
from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.service import codeService
from typing import List

router = APIRouter(
    prefix="/code",
)

DB = Annotated[Session, Depends(get_db)]


@router.get("/select-code")
def select_code(db: DB, request: Request):
    param = dict(request.query_params)
    return codeService.select_code(db, param)
