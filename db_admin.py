"""methods for administering the database directly: adding people or viewing records"""

import csv
from pathlib import Path

import database


MENU_PROMPT = """--- Database Admin ---

Please choose one of these options:

1) Add a new person
2) Add many new people
3) Display all people from the db
4) Exit

Your selection: """


def main():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "4":
        match user_input:
            case "1":
                prompt_add_person(connection)
            case "2":
                prompt_add_many_people(connection)
            case "3":
                prompt_get_all_people(connection)
            case _:
                print("invalid choice, please try again")
                pass

def prompt_add_person(connection):
    "asks for a person's name and type then enters that person into the database"
    name = input("Enter person's name: ").lower()
    type = input("Enter what sort of person this is: ").lower()
    database.add_person(connection, (name.title(), type.title()))
    article = "an" if type[0] in ("aeiou") else "a"
    print(f"added {name.title()}, {article} {type}.")

def prompt_add_many_people(connection):
    "asks for a filepath then adds the people listed into the database"
    while True:
        file = Path(input("Enter the filepath (must be a csv file): "))
        if file.exists() and file.suffix == ".csv":
            with open(file, "r") as csvfile:
                reader = csv.reader(csvfile)
                next(reader) # skip header row
                for row in reader:
                    database.add_person(connection, row)
                break
        else:
            print("File missing or wrong format")

def prompt_get_all_people(connection):
    "lists details of all people recorded in the database"
    print("Fetching all people from the database...")
    people = database.get_all_people(connection)
    for p in people:
        print(p)

if __name__ == '__main__':
    main()
