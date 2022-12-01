from flask import Blueprint, jsonify

from src.utils.errors_util import CommonError

error_route = Blueprint("error_route", __name__)


@error_route.app_errorhandler(CommonError)
def common_error(CommonError):
    return jsonify({"status": CommonError.message}), CommonError.status_code
