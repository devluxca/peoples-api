from app import db
from app.entities.people_entity import PeopleModel

from sqlalchemy.orm.exc import UnmappedInstanceError
from app.errors import NotFoundPeople

class DeletePeople:
    def execute(people_id: int):
        people = PeopleModel.query.filter_by(id = people_id).first()
        try:
            db.session.delete(people)
            db.session.commit()
        except UnmappedInstanceError as error:
            db.session.rollback()
            raise NotFoundPeople
