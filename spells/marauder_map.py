import os
import homework13
class MapMagic:

    __map_open = "I solemnly swear that I'm up to no good"
    __map_close = "Mischief managed"



class MarauderMap(MapMagic):
    def __init__(self, path):
        self.path = path


    def map_generator(self):

        hw_13 = homework13.film_awards_list()
        print(MapMagic.__map_open)
        print(MapMagic.__map_close)

    map_generator()

    __films_titles = {
        "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }


