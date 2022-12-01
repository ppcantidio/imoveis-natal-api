from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from src.schemas.users.broker_user import BrokerSchema

# from src.services.broker_service import BrokerService
from src.utils.response_util import ResponseUtil

broker_route = Blueprint("broker_route", __name__)


class BrokerRoute:
    @broker_route.route("/", methods=["GET"])
    def get_broker():
        return jsonify({"message": "hello wolrd"})

    @broker_route.route("/", methods=["POST"])
    def create_broket():
        req_data = request.get_json() or None

        try:
            broker_request = BrokerSchema().load(req_data)
        except ValidationError as err:
            return ResponseUtil.res_data_invalid(err.messages)

        return jsonify(broker_request)
