from flask import Flask
from flask_graphql import GraphQLView
# local imports
from .graphql import schema
from .db import db_session

app = Flask(__name__)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()