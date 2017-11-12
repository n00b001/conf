import sql

USER_ROW = "(`firstName`, `lastName`, `email`, `password`, `currentTitle`, `company`, `department`, `industry`, `bio`, `education`, `prevOrg`)"
USER_PREF_ROW = "(`userId`, `currentTitle`, `department`, `industry`)"
MATCH_ROW = "(`userId`, `connectedUserId`, `score`)"

def add_schedule(user, start_times):
    data = sql.get("UPDATE users set availability={} WHERE userID={}".format(start_times, user))

    return None


def get_matches(user):
    data = sql.get("""
SELECT  
M.connectedUserId, X.connectedUserId,
X.score + M.score Z

from Matches M
LEFT JOIN (SELECT connectedUserId, score from conf.Matches where userID='{}') X ON M.userId = X.connectedUserId
where M.connectedUserId='{}';    
    """.format(user, user))
    return data


def get_user_prefs():
    data = sql.get("SELECT * from userprefs")
    return data


def add_user(user, profile):
    data = sql.get("INSERT INTO `USERS` {} VALUES {}".format(USER_ROW, profile))
    # data = sql.get("")
    return None


def add_preference(user, preference):
    data = sql.get("INSERT INTO `UserPrefs` {} VALUES {}".format(USER_PREF_ROW, preference))
    return None


def add_match(userId, connectedUserId, score):
    data = sql.get("INSERT INTO `Matches` {} VALUES ('{}', '{}', '{}')".format(MATCH_ROW, userId,
                                                                               connectedUserId, score))
    return None

def main():
    for x in range(1, 1001):
        matches = get_matches(x)
        filtered = [x for x in matches if x["Z"] is not None and int(x["Z"]) > 1]
        if len(filtered) > 0:
            pass
        pass

if __name__ == '__main__':
    main()