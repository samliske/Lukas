from website import create_app
from website import models
from os import path
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

app = create_app()

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')



if __name__ == '__main__':
    app.run(debug=True)


