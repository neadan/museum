import logging
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from repository.entities import City

logfile = open('museum.log', 'a', encoding='utf-8')
logging.basicConfig(stream=logfile,
    level=logging.INFO,
    format='%(asctime)s - %(message)s')

class Database():
    def __init__(self, connect_string):
        postgres_engine = db.create_engine(connect_string)
        Session = sessionmaker(bind=postgres_engine)
        self.session = Session()

    def save(self, model):
        logging.info("Saving {}".format(model))
        self.session.merge(model)
        self.session.commit()

    def contains_city(self, city):
        return self.session.query(City).get(city) is not None
