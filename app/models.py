from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=20), unique=True, index=True)
    hashed_password = Column(String(length=100))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=30), index=True)
    description = Column(String(length=50), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}