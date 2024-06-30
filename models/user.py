from typing import Optional

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __table_name__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                    auto_increment=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Optional[Mapped[str]]
