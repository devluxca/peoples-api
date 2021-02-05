from app import db
from app.entities.people_entity import PeopleModel, People
from app.entities.franchisor_entity import FranchisorModel
from app.errors import EmailAlreadyExists, NotFoundFranchisor

class CreatePeople:
    def execute(data_request):
        validatedPeople = People(**data_request).dict(exclude_none=True)
        people = PeopleModel(**validatedPeople)

        franchisor = FranchisorModel.query.filter_by(id=validatedPeople['franchisor_id']).first()
        emailAlreadyExists = PeopleModel.query.filter_by(email=validatedPeople['email']).first()

        if emailAlreadyExists:
            raise EmailAlreadyExists
        if not franchisor: 
            raise NotFoundFranchisor

        try:
            db.session.add(people)
            db.session.commit()
        except Exception as err:
            print(err)
            db.session.rollback()

