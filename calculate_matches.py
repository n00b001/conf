import traceback

import runner
import sql


def is_empty(user):
    return len(user) == 0


def main():
    usr_pref = runner.get_user_prefs()
    for item in usr_pref:
        try:
            data = sql.get("SELECT * from users where currentTitle='{}' and department='{}' and industry='{}'"
                           .format(item["currentTitle"], item["department"], item["industry"]))
            for match in data:
                runner.add_match(item["userId"], match["userId"], 3)

            data = sql.get("SELECT * from users where currentTitle='{}' and department='{}'"
                           .format(item["currentTitle"], item["department"]))
            for match in data:
                runner.add_match(item["userId"], match["userId"], 2)

            data = sql.get("SELECT * from users where currentTitle='{}' and industry='{}'"
                       .format(item["currentTitle"], item["industry"]))
            for match in data:
                runner.add_match(item["userId"], match["userId"], 2)

            data = sql.get("SELECT * from users where department='{}'"
                       .format(item["department"]))
            for match in data:
                runner.add_match(item["userId"], match["userId"], 1)

            data = sql.get("SELECT * from users where industry='{}'"
                       .format(item["industry"]))
            for match in data:
                runner.add_match(item["userId"], match["userId"], 1)

            data = sql.get("SELECT * from users where currentTitle='{}'"
                       .format(item["currentTitle"]))
            for match in data:
                runner.add_match(item["userId"], match["userId"], 1)
        except Exception as e:
            traceback.print_exc()
            print(e)


    pass


if __name__ == '__main__':
    main()
