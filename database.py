import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from repository.entities import City


class Database():
    def __init__(self, connect_string):
        postgres_engine = db.create_engine(connect_string)
        Session = sessionmaker(bind=postgres_engine)
        self.session = Session()

    def save(self, model):
        self.session.merge(model)
        self.session.commit()

    def contains(self, city):
        return self.session.query(City).get(city) is not None
