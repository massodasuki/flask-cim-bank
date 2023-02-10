
from flask import Blueprint, request, jsonify
import sys
routers_blueprint = Blueprint('urls', __name__,)

from customer import db, CustomerProfile
"""
Get All Customer
"""

@routers_blueprint.route("/customers", methods=['GET'])
def get_all_customers():
    # customers = CustomerProfile.query.all()
    return CustomerProfile.fs_get_delete_put_post()


"""
Get Customer By Id
"""


@routers_blueprint.route("/customers/<id>", methods=['GET'])
def get_customer(id):
    customer = CustomerProfile.query.get(id)

    if customer:
        return CustomerProfile.fs_get_delete_put_post(id)
    else:
        return jsonify({
            "code": 404,
            "error": "Customer profile not found."
        })


"""
Create Customer
"""




@routers_blueprint.route("/customers", methods=['POST'])
def add_customer():
    data = request.get_json()

    name = data.get('name')
    date_of_birth = data.get('date_of_birth')
    address = data.get('address')
    phone_number = data.get('phone_number')
    email = data.get('email')
    income = data.get('income')
    employment_status = data.get('employment_status')
    loan_history = data.get('loan_history')
    bank_account_info = data.get('bank_account_info')
    government_issued_id = data.get('government_issued_id')
    age = data.get('age')
    gender = data.get('gender')
    education = data.get('education')
    occupation = data.get('occupation')
    marital_status = data.get('marital_status')
    spending_habits = data.get('spending_habits')
    payment_history = data.get('payment_history')
    transaction_frequency = data.get('transaction_frequency')

    new_customer = CustomerProfile(
        name=name,
        date_of_birth=date_of_birth,
        address=address,
        phone_number=phone_number,
        email=email,
        income=income,
        employment_status=employment_status,
        loan_history=loan_history,
        bank_account_info=bank_account_info,
        government_issued_id=government_issued_id,
        age=age,
        gender=gender,
        education=education,
        occupation=occupation,
        marital_status=marital_status,
        spending_habits=spending_habits,
        payment_history=payment_history,
        transaction_frequency=transaction_frequency
    )

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({
            "code": 201,
            "message": "Customer profile created successfully."
        })
    except Exception as e:
        return jsonify({
            "code": 400,
            "error": str(e.orig)
        })


"""
Update Customer
"""


@routers_blueprint.route("/customers/<id>", methods=['PUT'])
def update_customer(id):
    customer = CustomerProfile.query.get(id)
    if customer:
        data = request.get_json()

        customer.name = data.get('name', customer.name)
        customer.date_of_birth = data.get('date_of_birth', customer.date_of_birth)
        customer.address = data.get('address', customer.address)
        customer.phone_number = data.get('phone_number', customer.phone_number)
        customer.email = data.get('email', customer.email)
        customer.income = data.get('income', customer.income)
        customer.employment_status = data.get('employment_status', customer.employment_status)
        customer.loan_history = data.get('loan_history', customer.loan_history)
        customer.bank_account_info = data.get('bank_account_info', customer.bank_account_info)
        customer.government_issued_id = data.get('government_issued_id', customer.government_issued_id)
        customer.age = data.get('age', customer.age)
        customer.gender = data.get('gender', customer.gender)
        customer.education = data.get('education', customer.education)
        customer.occupation = data.get('occupation', customer.occupation)
        customer.marital_status = data.get('marital_status', customer.marital_status)
        customer.spending_habits = data.get('spending_habits', customer.spending_habits)
        customer.payment_history = data.get('payment_history', customer.payment_history)
        customer.transaction_frequency = data.get('transaction_frequency', customer.transaction_frequency)

        try:
            db.session.commit()
            return jsonify({
                "code": 204,
                "message": "Customer profile updated successfully."
            })
        except Exception as e:
            return jsonify({
                "code": 400,
                "error": str(e.orig)
            })
    else:
        return jsonify({
            "code": 404,
            "error": "Customer profile not found."
        })


"""
Delete Customer
"""

@routers_blueprint.route("/customers/<id>", methods=['DELETE'])
def delete_customer(id):
    customer = CustomerProfile.query.get(id)
    if customer:
        try:
            db.session.delete(customer)
            db.session.commit()
            return jsonify({
                "code": 204,
                "message": "Customer profile deleted successfully."
            })
        except Exception as e:
            return jsonify({
                "code": 400,
                "error": str(e.orig)
            })
    else:
        return jsonify({
            "code": 404,
            "error": "Customer profile not found."
        })
