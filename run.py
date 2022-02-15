from app.app import app, register_blueprints

if __name__ == "__main__":
    register_blueprints(app)

    app.run(host="localhost", port=3000, debug=True)