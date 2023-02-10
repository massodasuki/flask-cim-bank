from flask import Flask
from router import routers_blueprint
import config
from customer import db
from flask_migrate import Migrate

app = Flask(__name__)
app.register_blueprint(routers_blueprint)
app.debug = config.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)