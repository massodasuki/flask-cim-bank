# Customer Information Management (Banking)

This app include with REST API which has the following endpoint:
 
##### 1. Register new customer

This endpoint allows you to create a new customer account by submitting the required information

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

##### 2. View customer detail

This endpoint enables you to retrieve information about a specific customer by sending a request with the customer ID. 

http://localhost:5000/customers/:id

```
curl --location --request GET 'http://localhost:5000/customers/:id'
```

##### 3. Update customer detail

This endpoint allows you to modify an existing customer's information by sending a request with the updated details

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

##### 4. Delete customer detail

This endpoint enables you to delete a customer's account from the system by sending a request with the customer's id. Note that deleting a customer's account is a permanent action and cannot be undone

http://localhost:5000/customers/:id

```
curl --location --request DELETE 'http://localhost:5000/customers/:id'

```

## POSTMAN

Postman is a standalone software testing API (Application Programming Interface) platform to build, test, design, modify, and document APIs.

You may download Postman at this link : https://www.postman.com/downloads/

The postman collection can be find at here https://github.com/massodasuki/flask-cim-bank/blob/main/Flask%20Bank%20CIM.postman_collection.json

Then import this Postman collection by using this tutorial : https://learning.postman.com/docs/getting-started/importing-and-exporting-data/

## How to RUN the application

This application is made with Python 3.10.6

Clone this app

```
$ git clone https://github.com/massodasuki/flask-cim-bank.git
$ cd flask-cim-bank
```

Activate virtual environment

```
$ source env/bin/activate
```


This repo included the dependencies, so this command seem not needed for right now (I am too lazy to make gitignore file. Sorry)
```
$ pip install -r requirements.txt
```


Make flask migration (postgresql)

```
$ flask db init
$ flask db upgrade
$ flask db migrate
```

Finally run the app 

```
$ flask run
```

Then the app can be access at local http://localhost:5000


