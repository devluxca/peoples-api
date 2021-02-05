from flask import request, render_template
from app import app, db
from app.entities.franchisor_entity import FranchisorModel, Franchisor
from pydantic import ValidationError
from typing import List

from app.services.franchisor.create_franchisor import CreateFranchisor
from app.services.franchisor.get_franchisor import GetFranchisorByPage, GetFranchisorByID
from app.services.franchisor.delete_franchisor import DeleteFranchisor
from app.services.franchisor.update_franchisor import UpdateFranchisor

from app.errors import NotFoundFranchisor, NotFoundBodyRequest
from sqlalchemy.exc import InvalidRequestError


@app.route('/api/v1/franchisor/<int:page>')
@app.route('/api/v1/franchisor', methods=['GET'])
def get_franchisor(page: int = 1):
    franchisors = GetFranchisorByPage.execute(page)
    return { 'results': franchisors['franchisor_list'], 'total_pages': franchisors['total_pages'] }

@app.route('/api/v1/franchisor/show/<int:franchisor_id>')
def show_franchisor(franchisor_id: int):
    try:
        franchisor = GetFranchisorByID.execute(franchisor_id)
        return franchisor, 200
    except NotFoundFranchisor as error:
        return error.message, error.http_code

@app.route('/api/v1/franchisor', methods=['POST'])
def create_franchisor():
    try:
        CreateFranchisor.execute(request.json)
        return '', 201
    except ValidationError as error:
        return error.json()

@app.route('/api/v1/franchisor/<int:franchisor_id>', methods=['PUT'])
def update_franchisor(franchisor_id: int):
    try:
        UpdateFranchisor.execute(request.json, franchisor_id)

        return '', 200
    except NotFoundFranchisor as error:
        return error.message, error.http_code
    except NotFoundBodyRequest as error:
        return error.message, error.http_code
    except InvalidRequestError as error:
        return '', 400

@app.route('/api/v1/franchisor/<int:franchisor_id>', methods=['DELETE'])
def delete_franchisor(franchisor_id: int):
    try:
        DeleteFranchisor.execute(franchisor_id)
        return '', 200
    except NotFoundFranchisor as error:
        return error.message, error.http_code

@app.route('/franchisor', methods=['GET'])
def view_franchisor():
    page = request.args.get('page') or 1
    franchisors = GetFranchisorByPage.execute(page)
    return render_template('franchisor.html', **franchisors, page=int(page))