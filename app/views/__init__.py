from flask import Flask

def init_app(app: Flask):
    from .cep_view import bp_cep as cep
    app.register_blueprint(cep)