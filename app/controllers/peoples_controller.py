from flask import request, render_template
from app import app
from app.entities.people_entity import PeopleModel, People
from pydantic import ValidationError

from app.services.people.create_people import CreatePeople
from app.services.people.get_people import GetPeopleByPage, GetPeopleByID
from app.services.people.delete_people import DeletePeople
from app.services.people.update_people import UpdatePeople

from app.errors import EmailAlreadyExists, NotFoundFranchisor, NotFoundPeople, NotFoundBodyRequest
from sqlalchemy.exc import InvalidRequestError

@app.route('/api/v1/people/<int:page>')
@app.route('/api/v1/people', methods=['GET'])
def get_peoples(page:int = 1):
    peoples = GetPeopleByPage.execute(page)
    return { 'results': peoples['peoples_list'], 'total_pages': peoples['total_pages'] }

@app.route('/api/v1/people/show/<int:people_id>')
def show_people(people_id: int):
    try:
        people = GetPeopleByID.execute(people_id)
        return people, 200
    except NotFoundPeople as error:
        return error.message, error.http_code
    

@app.route('/api/v1/people', methods=['POST'])
def create_people():
    try:
        CreatePeople.execute(request.json)
        return '', 201
    except ValidationError as error:
        return error.json(), 400
    except NotFoundFranchisor as error:
        return error.message, error.http_code
    except EmailAlreadyExists as error:
        return error.message, error.http_code

@app.route('/api/v1/people/<int:people_id>', methods=['PUT'])
def update_people(people_id: int):
    try:
        UpdatePeople.execute(request.json, people_id)

        return '', 200
    except NotFoundPeople as error:
        return error.message, error.http_code
    except NotFoundFranchisor as error:
        return error.message, error.http_code
    except EmailAlreadyExists as error:
        return error.message, error.http_code
    except NotFoundBodyRequest as error:
        return error.message, error.http_code
    except InvalidRequestError as error:
        return '', 400
    except ValidationError as error:
        return error.json(), 400

@app.route('/api/v1/people/<int:people_id>', methods=['DELETE'])
def delete_people(people_id: int):
    try:
        DeletePeople.execute(people_id)
        return '', 200
    except NotFoundPeople as error:
        return error.message, error.http_code

@app.route('/people', methods=['GET'])
def view_people():
    page = request.args.get('page') or 1
    peoples = GetPeopleByPage.execute(page)
    return render_template('people.html', **peoples, page=int(page))
    