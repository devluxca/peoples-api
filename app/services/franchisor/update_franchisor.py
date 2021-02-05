from app import db
from app.entities.franchisor_entity import FranchisorModel, Franchisor

from app.errors import NotFoundBodyRequest, NotFoundFranchisor
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import InvalidRequestError

class UpdateFranchisor:
    def execute(data_request, franchisor_id: int):
        try:
            validatedFranchisor = Franchisor(**data_request).dict(exclude_none=True)
            
            updatedStatus = FranchisorModel.query.filter_by(id = franchisor_id).update(validatedFranchisor)
            if updatedStatus == 0:
                raise NotFoundFranchisor

            db.session.commit()
        except TypeError as error:
            raise NotFoundBodyRequest
        except UnmappedInstanceError as error:
            raise NotFoundFranchisor
        except InvalidRequestError as error:
            raise InvalidRequestError