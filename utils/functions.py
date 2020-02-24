import qwikidata
import qwikidata.sparql
from time import sleep

country_dict = {"NED": "Netherlands",
                "VAT": "Vatican City",
                "ESP": "Spain",
                "TWN": "Taiwan",
                "UK": "United Kingdom",
                "US": "United States of America",
                "RUS": "Russia",
                "POL": "Poland",
                "TUR": "Turkey",
                "AUS": "Australia",
                "FRA": "France",
                "CHN": "China",
                "KOR": "South Korea",
                "ITA": "Italy",
                "JPN": "Japan",
                "MEX": "Mexico"}


def get_city_population(city, country):
    if city == "Xi'an":
        return 12005600
    if city == 'Houston':
        return 2325502
    query = """
    SELECT ?city ?cityLabel ?country ?countryLabel ?population
    WHERE
    {
      ?city rdfs:label '%s'@en.
      ?city wdt:P1082 ?population.
      ?city wdt:P17 ?country.
      ?city rdfs:label ?cityLabel.
      ?country rdfs:label ?countryLabel.
      FILTER(LANG(?cityLabel) = "en").
      FILTER(LANG(?countryLabel) = "en").
      FILTER(CONTAINS(?countryLabel, "%s")).
    }
    """ % (city, country)

    res = qwikidata.sparql.return_sparql_query_results(query)
    out = res['results']['bindings'][0]
    sleep(1)
    return int(out['population']['value'])