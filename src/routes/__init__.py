def set_routes(app):
    @app.route("/")
    def hello_world():
        return "Hey bitches"
