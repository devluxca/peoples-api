from app import db
from app.entities.franchisor_entity import FranchisorModel, Franchisor

class CreateFranchisor:
    def execute(data_request):
        validatedFranchisor = Franchisor(**data_request).dict(exclude_none=True)
        franchisor = FranchisorModel(**validatedFranchisor)
        
        try:
            db.session.add(franchisor)
            db.session.commit()
        except:
            db.session.rollback()
