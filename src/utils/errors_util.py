class CommonError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = int(status_code)
