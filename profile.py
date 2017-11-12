from peewee import CharField


class Profile:
    userID = CharField()
    job_title = CharField()
    organisation = CharField()
    organisation_industry = CharField()
    organisation_category = CharField()
    department = CharField()
    education = CharField()
    previous_organisations = CharField()

    def __init__(self, userID, json):
        self.userID = userID
        self.job_title = json["job_title"]
        self.organisation = json["organisation"]
        self.organisation_industry = json["organisation_industry"]
        self.organisation_category = json["organisation_category"]
        self.department = json["department"]
        self.education = json["education"]
        self.previous_organisations = json["previous_organisations"]
