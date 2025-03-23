from routes import app

def create_app():
    return app


if __name__ == '__main__':
    app.run(debug=True)