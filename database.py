import sqlite3


"""sql queries and methods for interacting with the database"""


CREATE_PEOPLE_TABLE = "CREATE TABLE IF NOT EXISTS people (person_id INTEGER PRIMARY KEY, name TEXT, type TEXT, rating INTEGER, appearances INTEGER)"
INSERT_PERSON = "INSERT INTO people (name, type, rating, appearances) VALUES (?, ?, ?, ?)"
COUNT_PEOPLE = "SELECT COUNT(*) FROM people"
RECORD_APPEARANCE = "UPDATE people SET appearances = appearances + 1 WHERE person_id = ?"
RATE_PERSON = "UPDATE people SET rating = rating + 1 WHERE person_id = ?"
GET_ALL_PEOPLE = "SELECT person_id, name, type, CAST(rating AS FLOAT)/appearances AS score FROM people"
GET_PERSON_BY_NAME = "SELECT person_id, name, type, CAST(rating AS FLOAT)/appearances AS score FROM people WHERE name = ?"
GET_PERSON_BY_ID = "SELECT person_id, name, type, CAST(rating AS FLOAT)/appearances AS score FROM people WHERE person_id = ?"
GET_WORST_PERSON = "SELECT person_id, name, type, CAST(rating AS FLOAT)/appearances AS score FROM people ORDER BY score DESC LIMIT 1"
GET_WORST_TEN = "SELECT person_id, name, type, CAST(rating AS FLOAT)/appearances AS score FROM people ORDER BY score DESC LIMIT 10"

def connect():
    "connects to the database"
    return sqlite3.connect("data.db")

def create_tables(connection):
    "creates the people table if it doesn't already exist"
    with connection:
        connection.execute(CREATE_PEOPLE_TABLE)

def add_person(connection, args):
    "adds a person into the database"
    with connection:
        name, type = args
        connection.execute(INSERT_PERSON, (name, type, 0, 0))

def get_number_of_people(connection):
    "returns the number of people in the database"
    with connection:
        return connection.execute(COUNT_PEOPLE).fetchone()

def get_all_people(connection):
    "returns details of all people in the database"
    with connection:
        return connection.execute(GET_ALL_PEOPLE).fetchall()

def get_person_by_name(connection, name):
    "returns details of a named person"
    with connection:
        return connection.execute(GET_PERSON_BY_NAME, (name,)).fetchone()

def get_person_by_id(connection, person_id):
    "returns details of a person matching the given person_id"
    with connection:
        return connection.execute(GET_PERSON_BY_ID, (person_id,)).fetchone()

def get_worst_person(connection):
    "returns details of the person with the highest score in the database"
    with connection:
        return connection.execute(GET_WORST_PERSON).fetchone()

def get_worst_ten(connection):
    "returns details of the people with the ten highest scores in the database"
    with connection:
        return connection.execute(GET_WORST_TEN).fetchall()

def record_appearance(connection, person_id):
    "increments the given person's appearances by 1"
    with connection:
        connection.execute(RECORD_APPEARANCE, (person_id,))

def rate_person(connection, person_id):
    "increments the given person's rating by 1"
    with connection:
        connection.execute(RATE_PERSON, (person_id,))
