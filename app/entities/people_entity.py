from typing import List, Optional
from app import db
from pydantic import BaseModel, constr
from app.entities.franchisor_entity import Franchisor

class PeopleModel(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(256))
    email = db.Column(db.String(120), index=True, unique=True)

    franchisor_id = db.Column(db.Integer, db.ForeignKey('franchisor.id'), nullable=False)
    franchisor = db.relationship('FranchisorModel', backref=db.backref('peoples', lazy=True, cascade="all,delete"), uselist=False)

    def __repr__(self):
        return '<People {}>'.format(self.email)

class People(BaseModel):
    id: Optional[int]
    full_name: str
    email: str

    franchisor_id: int

    class Config:
        orm_mode = True