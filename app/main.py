import wikitables
import logging

from repository.entities import Museum, City
from app.database import Database
from app.utils import get_city_population, country_dict

from yoyo import read_migrations
from yoyo import get_backend

logfile = open('museum.log', 'a', encoding='utf-8')
logging.basicConfig(stream=logfile,
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def main(db_string):
    db = Database(db_string)
    wiki_page = "List of most visited museums"
    logging.info("Importing {}...".format(wiki_page))
    museum_table = wikitables.import_tables(wiki_page)[0]
    logging.info("Parsing table...")
    for row in museum_table.rows:
        country = str(row['Country flag, city']).split(" ")[0]
        city = " ".join(str(row['Country flag, city']).split(" ")[1:])
        if not db.contains_city(city):
            city_entity = City(name=city, country=country, population=get_city_population(city, country_dict.get(country)))
            db.save(city_entity)
        else:
            logging.info("{} already in database...skipping".format(city))

        museum_entity = Museum(name=_fix_museum_name(str(row['Name'])), city=city, yearlyvisitors=int(str(row['Visitors per year'])))
        db.save(museum_entity)


# wikitables API returns the reference in the museum name for some reason, but only for this museum
def _fix_museum_name(name):
    if name.startswith('National Palace Museum'):
        name = 'National Palace Museum'
    return name


# PRC == CHN
def _fix_country(country):
    if country == 'PRC':
        return 'CHN'


if __name__ == '__main__':
    db_str = 'postgresql://postgres:postgres@localhost/db_museum'
    backend = get_backend(db_str)
    migrations = read_migrations('migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    main(db_str)
