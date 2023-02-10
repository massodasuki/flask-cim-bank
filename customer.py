from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerialize

db = SQLAlchemy()

fs_mixin = FlaskSerialize(db)
"""
Define the Customer model
"""

class CustomerProfile(fs_mixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    income = db.Column(db.Float, nullable=False)
    employment_status = db.Column(db.String(50), nullable=False)
    loan_history = db.Column(db.String(100), nullable=False)
    bank_account_info = db.Column(db.String(100), nullable=False)
    government_issued_id = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    education = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    marital_status = db.Column(db.String(50), nullable=False)
    spending_habits = db.Column(db.String(100), nullable=False)
    payment_history = db.Column(db.String(100), nullable=False)
    transaction_frequency = db.Column(db.String(100), nullable=False)

    # serializer fields
    __fs_create_fields__ = __fs_update_fields__ = ['name',
                                                    'date_of_birth',
                                                    'address',
                                                    'phone_number',
                                                    'email',
                                                    'income',
                                                    'employment_status',
                                                    'loan_history',
                                                    'bank_account_info',
                                                    'government_issued_id',
                                                    'age',
                                                    'gender',
                                                    'education',
                                                    'occupation',
                                                    'marital_status',
                                                    'spending_habits',
                                                    'payment_history',
                                                    'transaction_frequency']

    
    # checks if Flask-Serialize can delete
    def __fs_can_delete__(self):
        if self.value == '1234':
            raise Exception('Deletion not allowed.  Magic value!')
        return True

    # checks if Flask-Serialize can create/update
    def __fs_verify__(self, create=False):
        if len(self.key or '') < 1:
            raise Exception('Missing key')

        if len(self.setting_type or '') < 1:
            raise Exception('Missing setting type')
        return True

    def __repr__(self):
        return '<CustomerProfile %r %r %r>' % (self.id, self.name, self.phone_number)

    def __repr__(self):
        return f'<CustomerProfile {self.name}>'
