from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from models.ml import MLLog


class MLRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    def add(self, **kwargs):
        with self.session_factory() as session:
            ml_log = MLLog(**kwargs)
            session.add(ml_log)
            session.commit()
            session.refresh(ml_log)
            return ml_log
