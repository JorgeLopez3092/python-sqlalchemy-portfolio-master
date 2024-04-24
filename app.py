from flask import (render_template, redirect,
                   url_for, request)
from werkzeug import Response
from models.Project import Project
from models.database import db, app

import os


@app.route('/')
def index() -> str:
    # return 'hello world!'
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new')
def project_create() -> str:
    return 'Hello World!'


@app.route('/projects/<id>')
def project_details(id) -> str:
    project = Project.query.get_or_404(id)
    project_skills = project.skills.split(',')
    date = project.date.strftime("%b %Y")
    return render_template('detail.html', project=project, project_skills=project_skills, date=date)


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
