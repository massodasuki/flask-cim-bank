import logging
import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "localhost")
POSTGRES = {
    "user": os.getenv("APPLICATION_POSTGRES_USER", "postgres"),
    "pw": os.getenv("APPLICATION_POSTGRES_PW", "mysecretpassword"),
    "host": os.getenv("APPLICATION_POSTGRES_HOST", DB_CONTAINER),
    "port": os.getenv("APPLICATION_POSTGRES_PORT", 5439),
    "db": os.getenv("APPLICATION_POSTGRES_DB", "postgres"),
}
DB_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
