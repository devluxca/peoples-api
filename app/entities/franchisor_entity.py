from app import db
from pydantic import BaseModel
from typing import Optional

class FranchisorModel(db.Model):
    __tablename__ = 'franchisor'
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<Franchisor {}>'.format(self.name)

class Franchisor(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True