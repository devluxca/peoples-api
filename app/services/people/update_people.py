from app import db
from app.entities.people_entity import PeopleModel, People
from app.entities.franchisor_entity import FranchisorModel

from app.errors import NotFoundBodyRequest, NotFoundPeople, NotFoundFranchisor, EmailAlreadyExists
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import InvalidRequestError

class UpdatePeople:
    def execute(data_request, people_id: int):
        try:
            validatedPeople = People.construct(**data_request).dict(exclude_none=True)

            if validatedPeople['franchisor_id']:
                franchisor = FranchisorModel.query.filter_by(id = validatedPeople['franchisor_id']).first()
                if not franchisor:
                    raise NotFoundFranchisor

            if validatedPeople['email']:
                emailAlreadyExists = PeopleModel.query.filter_by(email = validatedPeople['email']).first()
                if emailAlreadyExists:
                    raise EmailAlreadyExists

            updatedStatus = PeopleModel.query.filter_by(id = people_id).update(validatedPeople)
            if updatedStatus == 0:
                raise NotFoundPeople

            db.session.commit()
        except TypeError as error:
            raise NotFoundBodyRequest
        except UnmappedInstanceError as error:
            raise NotFoundPeople
        except InvalidRequestError as error:
            raise InvalidRequestError