from flask import jsonify


class ResponseUtil:
    @staticmethod
    def res_data_invalid(error):
        response = jsonify({"message": error})
        return response

    @staticmethod
    def res_data_success(data):
        response = jsonify({"message": "Data retrived with success", "data": data})
        return response

    @staticmethod
    def res_sucess(message):
        response = jsonify({"message": message})
        return response
