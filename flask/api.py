from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from compound import compound_yearly_value_with_interest

app = Flask(__name__)
api = Api(app)


class CompoundInterest(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        present_value = json_data['present_value']
        rate = json_data['interest_rate']
        time = json_data['time']
        fv = compound_yearly_value_with_interest(present_value, rate, time)

        return jsonify(future_value=fv)


api.add_resource(CompoundInterest, '/compoundinterest')

if __name__ == '__main__':
    app.run(debug=True)
