from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

# initialize SQLAlchemy metadata
metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# import models here/define your models here
class Students(db.Model):
    # define table
    __tablename__ = "students"

    # define columns
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.test, nullable=False)
    last_name = db.Column(db.text, nullable=False)
    email = db.Column(db.String[100], nullable=False)
    