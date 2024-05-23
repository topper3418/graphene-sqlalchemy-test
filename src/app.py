from flask import Flask
from flask_graphql import GraphQLView
# local imports
from .db import db
from graphql import schema


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///household.db"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)


