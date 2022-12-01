from flask import jsonify


class ResponseUtil:
    @staticmethod
    def res_data_invalid(error):
        response = jsonify({"message": error})
        return response
