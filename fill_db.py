import random
import string
import traceback

import runner

names = []
with open("names.txt", "r") as f:
    names = [x.split(" ")[0].strip() for x in f.readlines()]

jobTitles = []
with open("jobs.csv", "r") as f:
    jobTitles = [x.split(",")[1].strip() for x in f.readlines()]

companies = []
with open("businesses.txt", "r") as f:
    companies = [x.strip() for x in f.readlines()]

industry = []
with open("industries.txt", "r") as f:
    industry = [x.strip() for x in f.readlines()]

education = []
with open("education.txt", "r") as f:
    education = [x.strip() for x in f.readlines()]

department = []
with open("department.txt", "r") as f:
    department = [x.strip() for x in f.readlines()]


def get_userID():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(32))


def getemail():
    return getName().replace("'", "") + "@gmail.com"


def getName():
    return names[random.randint(0, len(names) - 1)].replace("\"", "").replace("'", "").replace(",", "").strip()


def getCurrecntTitle():
    return jobTitles[random.randint(0, len(jobTitles) - 1)].replace("\"", "").replace("'", "").strip()


def getCompany():
    return companies[random.randint(0, len(companies) - 1)].replace("\"", "").replace("'", "").strip()


def getIndustry():
    return industry[random.randint(0, len(industry) - 1)].replace("\"", "").replace("'", "").strip()


def getEducation():
    return education[random.randint(0, len(education) - 1)].replace("\"", "").replace("'", "").strip()


def getTimeDate():
    return "'',"


def getPrevOrg():
    return ",".join([str(getCompany()).replace("\"", "").replace("'", "").strip() for x in range(0, 3)])


def get_user_attrib():
    return "'" + getName() + "','" + getName() + "','" + getemail() + "','" + get_userID() + "','" + getCurrecntTitle() \
           + "','" + getCompany() + "','" + getDepartment() + "','" + getIndustry() + "','" + get_userID() + "','" + "\"" \
           + getEducation() + "\"" + "','" + "\"[" + getPrevOrg() + "]\"" + "\'"


def get_user():
    return '(' + get_user_attrib() + ')'


def getDepartment():
    return department[random.randint(0, len(department) - 1)].replace("\"", "").replace("'", "").strip()


def get_user_pref_attrib(userID):
    return "'" + str(userID) + "','" + getCurrecntTitle() + "','" + getDepartment() + "','" + getIndustry() + "'"


def get_pref(userID):
    return '(' + get_user_pref_attrib(userID) + ')'


def main():
    NUM_OF_USERS = 1001
    for x in range(1, NUM_OF_USERS):
        try:
            user = get_user()
            runner.add_user("", user)
        except Exception as e:
            traceback.print_exc()
            print(e)
    for x in range(1, NUM_OF_USERS):
        try:
            pref = get_pref(x)
            runner.add_preference("", pref)

            pref = get_pref(x)
            runner.add_preference("", pref)

            pref = get_pref(x)
            runner.add_preference("", pref)
        except Exception as e:
            traceback.print_exc()
            print(e)


if __name__ == '__main__':
    main()
