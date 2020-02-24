import wikitables

from repository.entities import Museum, City
from database import Database
from utils import get_city_population, country_dict

from yoyo import read_migrations
from yoyo import get_backend


def main(db_string):
    db = Database(db_string)
    museum_table = wikitables.import_tables('List of most visited museums')[0]
    for row in museum_table.rows:
        country = str(row['Country flag, city']).split(" ")[0]
        city = " ".join(str(row['Country flag, city']).split(" ")[1:])
        if not db.contains_city(city):
            city_entity = City(name=city, country=country, population=get_city_population(city, country_dict.get(country)))
            db.save(city_entity)
        else:
            print("{} already in database...skipping".format(city))

        museum = Museum(name=_fix_museum_name(str(row['Name'])), city=city, yearlyvisitors=int(str(row['Visitors per year'])))
        db.save(museum)


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
    db_string = 'postgresql://postgres:postgres@localhost/db_museum'
    backend = get_backend(db_string)
    migrations = read_migrations('migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    main(db_string)
