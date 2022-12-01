from src.routes.broker_route import broker_route
from src.routes.error_route import error_route


def init_app(app):
    """
    Register blueprints
    """
    app.register_blueprint(error_route)
    print("teste")
    app.register_blueprint(broker_route, url_prefix="/broker")
