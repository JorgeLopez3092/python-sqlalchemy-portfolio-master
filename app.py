from flask import (render_template, redirect,
                   url_for, request)
from werkzeug import Response
from models.Project import Project
from models.database import db, app


@app.route('/')
def index() -> str:
    print(app.template_folder)
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
