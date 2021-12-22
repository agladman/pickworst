from random import sample

import database
from db_admin import prompt_add_person

"""main file for users to interact with the app: add, score or view people"""

def retrieve_person(connection, person_id):
    "fetches a person from the database and records their appearance"
    database.record_appearance(connection, person_id)
    return database.get_person_by_id(connection, person_id)

def display_person(args):
    "displays a person's name and type in a readable format"
    _, name, type, score = args
    article = "an" if type[0] in ("aeiou") else "a"
    return f"{name}, {article} {type.lower()}"

def get_candidates(connection):
    "gets two candidates for scoring against one another"
    pool = database.get_number_of_people(connection)[0]
    a, b = sample(range(1, pool), 2)
    person_a = retrieve_person(connection, a)
    person_b = retrieve_person(connection, b)
    return (person_a, person_b)

def show_worst_person(connection):
    "displays the person in the database with the highest score"
    the_worst = database.get_worst_person(connection)
    print(f"The worst person is currently {display_person(the_worst)}.")

def show_worst_ten(connection):
    "displays the ten people in the database with the highest score"
    people = database.get_worst_ten(connection)
    for p in people:
        print(f"\t{p[3]:.2f} {display_person(p)}")

def present_choice(connection):
    "asks user to chose who is worst between two people"
    a, b = get_candidates(connection)
    while (vote := input(f"Who's worse, {display_person(a)} (1) or {display_person(b)} (2)? Or press (3) to exit: ")) != "3":
        match vote:
            case "1":
                database.rate_person(connection, a[0])
                break
            case "2":
                database.rate_person(connection, b[0])
                break
            case _:
                print("That's not a valid choice, please enter either 1 or 2")
    show_worst_person(connection)


def main():
    connection = database.connect()
    database.create_tables(connection)

    print("--- PICKWORST ---")

    show_worst_person(connection)

    start_menu = """
    What do you want to do?

    1) add a person to the list
    2) start rating people
    3) see the worst 10 people
    4) exit

    Your choice: """

    while (user_input := input(start_menu)) != "4":
        match user_input:
            case "1":
                prompt_add_person(connection)
            case "2":
                present_choice(connection)
            case "3":
                show_worst_ten(connection)
            case _:
                print("That's an invalid choice, pardner. Try again.")

if __name__ == '__main__':
    main()
