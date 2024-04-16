from flask import (render_template, redirect,
                   url_for, request)
from werkzeug import Response
from models.Project import Project
from models.database import db, app

import os


@app.route('/')
def index() -> str:
    print(app.template_folder)
    print(os.listdir('templates'))  # This should list all files in the templates directory
    print(os.path.isfile('templates/index2.html'))  # This should return True if the file exists
    # return 'hello world!'
    return render_template('index.html')


@app.route('/projects/new')
def project_create() -> str:
    return 'Hello World!'


@app.route('/projects/<id>')
def project_details() -> str:
    return 'Hello World!'


@app.route('/projects/<id>/edit')
def project_edit() -> str:
    return 'Hello World!'


@app.route('/projects/<id>/delete')
def project_delete() -> str:
    return 'Hello World!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
