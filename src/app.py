"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member_by_id(id):
    member = jackson_family.get_member(id)
    return_member = {
        "id": member["id"],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
    }

    return return_member, 200


@app.route('/member', methods=['POST'])
def add_new_member():
    request_body = request.get_json()
    member = jackson_family.add_member(request_body)

    # member = {
    #     "id" : body["id"],
    #     "age" : body["age"],
    #     "first_name": body["first_name"],
    #     #"last_name": jackson_family ,
    #     "lucky_numbers": body["lucky_numbers"]
    # }
    # jackson_family.add_member(member)
    return {}, 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    response = jackson_family.delete_member(id)
    if response == True:
        return jsonify({"done": True}), 200
    else:
        return 400







# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
