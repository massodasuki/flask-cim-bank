# Customer Information Management (Banking)

This REST API is created with following endpoint
 
1. Register new customer

http://localhost:5000/customers

```
curl --location --request POST 'http://localhost:5000/customers' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "name":"Masso",
    "date_of_birth": "1993-07-16",
    "address": "Shah Alam",
    "phone_number": "01131334193",
    "email":"massodasuki@gmail.com",
    "income":4000.00,
    "employment_status": "Private",
    "loan_history": "Affin",
    "bank_account_info": "12345648",
    "government_issued_id": "123456-78-9013",
    "age": 30,
    "gender": "Male",
    "education":"Master Degree",
    "occupation": "Software Engineer",
    "marital_status": "Married",
    "spending_habits": "Medium",
    "payment_history": "Excellent",
    "transaction_frequency": "Medium"
}'
```

2. View customer detail

http://localhost:5000/customers/:id

```
curl --location --request GET 'http://localhost:5000/customers/:id'
```

4. Update customer detail

http://localhost:5000/customers/:id

```
curl --location --request PUT 'http://localhost:5000/customers/:id' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "name":"Masso",
    "date_of_birth": "1993-07-16",
    "address": "Shah Alam",
    "phone_number": "01131334193",
    "email":"massodasuki@gmail.com",
    "income":4100.00,
    "employment_status": "Private",
    "loan_history": "Affin",
    "bank_account_info": "12345648",
    "government_issued_id": "123456-78-9013",
    "age": 30,
    "gender": "Male",
    "education":"Master Degree",
    "occupation": "Software Engineer",
    "marital_status": "Married",
    "spending_habits": "Medium",
    "payment_history": "Excellent",
    "transaction_frequency": "Medium"
}'
```

6. Delete customer detail
http://localhost:5000/customers/:id

```
curl --location --request DELETE 'http://localhost:5000/customers/:id'

```

The postman collection can be find at here https://github.com/massodasuki/flask-cim-bank/blob/main/Flask%20Bank%20CIM.postman_collection.json

## How to RUN 

```
$ source env/bin/activate
$ pip install -r requirements.txt
$ flask db init
$ flask db upgrade
$ flask db migrate
$ flask run
```

Then the web app can be access at local http://localhost:5000


