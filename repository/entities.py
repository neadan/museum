from sqlalchemy import Column, ForeignKey, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'
    name = Column(String, primary_key=True)
    country = Column(String)
    population = Column(BigInteger)

    def __repr__(self):
        return "City(name='{}', country='{}', population='{}')".format(self.name, self.country, self.population)


class Museum(Base):
    __tablename__ = 'museum'
    name = Column(String, primary_key=True)
    city = Column(String, ForeignKey('city.name'))
    yearlyvisitors = Column(BigInteger)

    def __repr__(self):
        return "Museum(name='{}', yearlyvisitors='{}', city='{}')".format(self.name, self.yearlyvisitors, self.city)