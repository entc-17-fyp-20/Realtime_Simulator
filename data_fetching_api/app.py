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
                row['time'] = i[1].isoformat()
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                last_30.append(row)
            return last_30
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
                row['time'] = i[1].isoformat()
                row['predicted'] = i[2]
                row['actual'] = i[3]
                row['difference'] = i[4]
                last_30.append(row)
            return last_30
        except Exception as e:
            print(e)
            return {'result': 'error'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
