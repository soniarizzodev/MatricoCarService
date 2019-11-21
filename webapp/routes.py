"""
Routes and views for the flask application.
"""

from flask import request
from webapp import app
from webapp.API.sync import sync

@app.route('/sync', methods=['GET', 'POST'])
def sync_api():
    data = request.get_json(force=True)

    if (data is not None):
        return sync(data)