from flask import Flask


app = Flask(
    __name__,
    template_folder="../frontend/build",
    static_folder="../frontend/build/static",
)


def create_app(config):
    app.config.from_object(config)

    with app.app_context():
        from . import routes

        return app
