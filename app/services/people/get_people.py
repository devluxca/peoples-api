from app.entities.people_entity import *
from math import ceil

from app.errors import NotFoundPeople

class GetPeopleByPage:
    def execute(page: int):
        page_size = 20

        total_pages = ceil(len(PeopleModel.query.all()) / page_size)
        peoples = PeopleModel.query.paginate(int(page), page_size).items
        peoples_list = [People.from_orm(people).dict() for people in peoples]
        return {'peoples_list': peoples_list, 'total_pages': total_pages }

class GetPeopleByID:
    def execute(people_id: int):
        people = PeopleModel.query.filter_by(id = people_id).first()
        if not people:
            raise NotFoundPeople
        return People.from_orm(people).dict()