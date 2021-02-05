from app import db
from app.entities.franchisor_entity import FranchisorModel

from sqlalchemy.orm.exc import UnmappedInstanceError
from app.errors import NotFoundFranchisor

class DeleteFranchisor:
    def execute(franchisor_id: int):
        franchisor = FranchisorModel.query.filter_by(id = franchisor_id).first()
        try:
            db.session.delete(franchisor)
            db.session.commit()
        except UnmappedInstanceError as error:
            db.session.rollback()
            raise NotFoundFranchisor
