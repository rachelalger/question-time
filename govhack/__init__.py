import logging

from flask import Flask, url_for, redirect

from werkzeug.contrib.cache import SimpleCache

from . import assets
from .database import db_session
from . import models

from flask.ext.cors import CORS

app = Flask(__name__, instance_relative_config=True)

#Initialise logging
logHandler = logging.StreamHandler()

logHandler.setLevel(logging.WARNING)

app.logger.addHandler(logHandler)

logger = logging.getLogger('govhack')

logger.addHandler(logHandler)

assets.register_assets(app)

CORS(app)

cache = SimpleCache()

import govhack.views


@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()
