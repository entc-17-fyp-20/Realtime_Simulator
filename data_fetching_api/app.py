from flask import Flask
from flask_restx import Api,Resource,fields
from utils.connect_db import *
import json
from flask_cors import CORS

app = Flask(__name__)
api = Api(app,version='1.0',title='Realtime simulator',description='Use this to test API call to DB')
CORS(app)


@api.route('/power')
class Power(Resource):
    def get(self):
        try:
            data = power_last_30()
            last_30 = []
            for i in data:
                row = {}
                row['id'] = i[0]
                time_list = i[1].isoformat().split("T")
                row['time'] = time_list[0] + " " + time_list[1]
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                last_30.append(row)
            return last_30[::-1]
        except Exception as e:
            print(e)
            return {'result': 'error'}


@api.route('/power_last')
class PowerLast(Resource):
    def get(self):
        try:
            data = power_last()
            last_one = []
            row = {}
            for i in data:
                row['id'] = i[0]
                time_list = i[1].isoformat().split("T")
                row['time'] = time_list[0] + " " + time_list[1]
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]

            data1 = power_last_30()
            avg_error = 0
            for i in data1:
                avg_error += abs(i[2] - i[3]) / i[3]
            avg_error = (100 * avg_error) / 30
            row['avg'] = avg_error
            last_one.append(row)
            return last_one
        except Exception as e:
            print(e)
            return {'result': 'error'}


@api.route('/power_last_2')
class PowerLast2(Resource):
    def get(self):
        try:
            data = power_last_2()
            last_two = []
            for i in data:
                row = {}
                row['id'] = i[0]
                time_list = i[1].isoformat().split("T")
                row['time'] = time_list[0] + " " + time_list[1]
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                last_two.append(row)
            last_two.pop(0)
            return last_two
        except Exception as e:
            print(e)
            return {'result': 'error'}


@api.route('/condition')
class Condition(Resource):
    def get(self):
        try:
            data = condition_last_30()
            last_30 = []
            for i in data:
                row = {}
                row['id'] = i[0]
                time_list = i[1].isoformat().split("T")
                row['time'] = time_list[0] + " " + time_list[1]
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                last_30.append(row)
            return last_30[::-1]
        except Exception as e:
            print(e)
            return {'result': 'error'}


@api.route('/condition_last')
class ConditionLast(Resource):
    def get(self):
        try:
            data = condition_last()
            last_one = []
            row = {}
            for i in data:
                row['id'] = i[0]
                time_list = i[1].isoformat().split("T")
                row['time'] = time_list[0] + " " + time_list[1]
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                if abs(int(i[4])) > 8:
                    status = "Unhealthy"
                else:
                    status = "Healthy"
                row['status'] = status

            data1 = condition_last_30()
            avg_error = 0
            for i in data1:
                avg_error += abs(i[2]-i[3])/i[3]

            avg_error = (100*avg_error)/30
            row['avg'] = avg_error
            last_one.append(row)
            return last_one
        except Exception as e:
            print(e)
            return {'result': 'error'}


@api.route('/condition_last_2')
class ConditionLast2(Resource):
    def get(self):
        try:
            data = condition_last_2()
            last_two = []
            for i in data:
                row = {}
                row['id'] = i[0]
                time_list = i[1].isoformat().split("T")
                row['time'] = time_list[0] + " " + time_list[1]
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                last_two.append(row)
            last_two.pop(0)
            return last_two
        except Exception as e:
            print(e)
            return {'result': 'error'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
