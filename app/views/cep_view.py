import requests

from http import HTTPStatus
from flask import Blueprint, request, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.configs.database import db
from app.models.cep_model import CepModel, CepSchema
from app.services import get_or_create_model, validate_city

bp_cep = Blueprint("cep_route", __name__)


@bp_cep.post("/cep")
def create_cep():
    try:
        data = request.get_json()
        cep_number = str(data.pop('cep'))
        url = f"http://viacep.com.br/ws/{cep_number}/json/"
        data = requests.get(url).json()
        if validate_city(data):
            data['validated'] = True
        my_cep = get_or_create_model(db.session, CepModel, **data)
        serializer = CepSchema().dump(my_cep['model'])
        if my_cep['exists']:
            return jsonify(serializer), HTTPStatus.OK
        if not my_cep['exists']:
            return jsonify(serializer), HTTPStatus.CREATED
    except KeyError:
        return jsonify({"erro": {"mensagem": "Você precisa inserir um formato e número válido para a requisição",
                                 "exemplo": "cep: 00000-000"}},
                       ), HTTPStatus.BAD_REQUEST
    except ValueError:
        return jsonify({"erro": {"mensagem": "O número inserido é inválido",
                                 "exemplo": "cep: 04117-091"}},
                       ), HTTPStatus.BAD_REQUEST


@bp_cep.get("/cep")
def all_cep():
    cep_schema = CepSchema(many=True)
    all_cep = CepModel.query.all()
    return jsonify(cep_schema.dump(all_cep)), HTTPStatus.OK


@bp_cep.get("/cep/<int:cep_id>")
def get_cep(cep_id):
    id = cep_id
    cep_schema = CepSchema()
    cep = CepModel.query.get(id)
    serializer = cep_schema.dump(cep)
    if serializer:
        return jsonify(serializer), HTTPStatus.OK
    if not serializer:
        return jsonify({"message": "Não existe um Cep com esse ID"}), HTTPStatus.NOT_FOUND


@bp_cep.delete("/cep/<int:cep_id>")
def delete_cep(cep_id):
    try:
        id = cep_id
        cep_model = CepModel()
        query = cep_model.query.get(id)
        db.session.delete(query)
        db.session.commit()
        return jsonify({"message": "Cep deletado com sucesso"}), HTTPStatus.OK
    except UnmappedInstanceError:
        return jsonify({"message": "O Id do Cep não existe no sistema"}), HTTPStatus.NOT_FOUND
