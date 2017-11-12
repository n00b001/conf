import flask_cors
from flask import Flask, request
from flask import json

import runner
from preference import Preference
from profile import Profile

app = Flask(__name__)
flask_cors.CORS(app)
MEETING_LENGTH_MINUTES = 30


@app.route('/', methods=['GET', 'POST'])
def root():
    print("root")

    data = ["root"]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/addUser', methods=['POST'])
def add_user():
    print("addUser")

    d = request.form
    user = get_field(d, "userID")
    profile = get_field(d, "profile")
    preferences = get_field(d, "preferences")

    data = runner.add_user(user, profile)
    data2 = runner.add_preference(user, preferences)

    response = app.response_class(
        response=json.dumps([data, data2]),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/getMatches', methods=['GET'])
def get_matches():
    print("getMatches")

    d = request.form
    user = get_field(d, "userID")

    data = runner.get_matches(user)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/addSchedules', methods=['POST'])
def add_schedules():
    print("addSchedules")

    d = request.form
    user = get_field(d, "userID")
    start_times = get_field(d, "times")
    end_times = [x + MEETING_LENGTH_MINUTES for x in start_times]

    data = runner.add_schedule(user, start_times)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response


def get_field(d, field):
    return json.loads(d[field])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
