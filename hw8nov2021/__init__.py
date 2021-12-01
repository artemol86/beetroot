import os
from flask import Flask


def create_app():
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)

    from . import server_08_11
    app.register_blueprint(server_08_11.bp)

    return app
