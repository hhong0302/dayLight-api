from app.core.dbUtils import transactional
from typing import List
from sqlalchemy.orm import Session
from app.repositories import codeRepository
from datetime import datetime
from app.core.messages import Msg


def select_code(db: Session, param: dict):
    return codeRepository.select_code(db, param)