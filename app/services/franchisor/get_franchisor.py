from app.entities.franchisor_entity import *
from math import ceil

from app.errors import NotFoundFranchisor

class GetFranchisorByPage:
    def execute(page: int):
        page_size = 20

        total_pages = ceil(len(FranchisorModel.query.all()) / page_size)
        franchisors = FranchisorModel.query.paginate(int(page), page_size).items
        franchisor_list = [Franchisor.from_orm(franchisor).dict() for franchisor in franchisors]
        return { 'franchisor_list': franchisor_list, 'total_pages': total_pages }

class GetFranchisorByID:
    def execute(franchisor_id: int):
        franchisor = FranchisorModel.query.filter_by(id = franchisor_id).first()
        if not franchisor:
            raise NotFoundFranchisor
        return Franchisor.from_orm(franchisor).dict()