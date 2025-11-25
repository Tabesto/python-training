# routes/companies.py
from flask import Blueprint, request, jsonify
from typing import List

from models.company import Company
from repositories.company_repo import CompanyRepository

# adapte le nom du module selon ton fichier : validation.schema vs validation.schemas
from validation.schema import CompanyCreate, CompanyUpdate, CompanyRead

bp_companies = Blueprint("companies", __name__, url_prefix="/companies")
repo = CompanyRepository()


@bp_companies.get("")
def list_companies():
    companies: List[Company] = repo.list()
    payload = [CompanyRead(**c.__dict__).model_dump() for c in companies]
    return jsonify(payload), 200


@bp_companies.post("")
def create_company():
    data = request.get_json() or {}
    schema = CompanyCreate(**data)

    company = Company(id=0, **schema.model_dump())
    created = repo.create(company)

    return jsonify(CompanyRead(**created.__dict__).model_dump()), 201


@bp_companies.get("/<int:company_id>")
def get_company(company_id: int):
    company = repo.get(company_id)
    if not company:
        return jsonify({"error": "Company not found"}), 404

    return jsonify(CompanyRead(**company.__dict__).model_dump()), 200


@bp_companies.put("/<int:company_id>")
def update_company(company_id: int):
    company = repo.get(company_id)
    if not company:
        return jsonify({"error": "Company not found"}), 404

    data = request.get_json() or {}
    schema = CompanyUpdate(**data)

    for field, value in schema.model_dump(exclude_unset=True).items():
        setattr(company, field, value)

    updated = repo.update(company_id, company)
    return jsonify(CompanyRead(**updated.__dict__).model_dump()), 200


@bp_companies.delete("/<int:company_id>")
def delete_company(company_id: int):
    ok = repo.delete(company_id)
    if not ok:
        return jsonify({"error": "Company not found"}), 404
    return "", 204
