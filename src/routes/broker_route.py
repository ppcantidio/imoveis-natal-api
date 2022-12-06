from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from src.schemas.users.broker_user import BrokerSchema

from src.services.broker_service import BrokerService
from src.utils.response_util import ResponseUtil

broker_route = Blueprint("broker_route", __name__)

service = BrokerService()
schema = BrokerSchema()


class BrokerRoute:
    @broker_route.route("/<uuid>", methods=["GET"])
    def get_broker(uuid):
        broker = service.get_user(uuid)
        return ResponseUtil.res_data_success(broker)

    @broker_route.route("/", methods=["POST"])
    def create_broket():
        req_data = request.get_json() or None

        try:
            broker_request = schema.load(req_data)
        except ValidationError as err:
            return ResponseUtil.res_data_invalid(err.messages)

        service.create_user(broker_request)

        return ResponseUtil.res_sucess("User created with success")
