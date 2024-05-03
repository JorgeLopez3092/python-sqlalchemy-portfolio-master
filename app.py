from flask import (render_template, redirect,
                   url_for, request)
from werkzeug import Response
from models.Project import Project
from models.database import db, app
import datetime


@app.context_processor
def inject_projects():
    projects = Project.query.all()
    return dict(projects=projects)


@app.route('/')
def index() -> str:
    # return 'hello world!'
    return render_template('index.html')


@app.route('/about')
def about() -> str:
    return render_template('about.html')


@app.route('/projects/new', methods=['GET', 'POST'])
def project_create() -> Response or str:
    if request.form:
        print(request.form['date'])
        date = datetime.datetime.strptime(request.form['date'], "%Y-%m")
        new_project: Project = Project(title=request.form['title'], description=request.form['desc'],
                                       skills=request.form['skills'], link=request.form['github'],
                                       date=date)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')
def project_details(id) -> str:
    project = Project.query.get_or_404(id)
    print(project.date)
    project_skills = project.skills.split(',')
    date = project.date.strftime("%b %Y")
    return render_template('detail.html', project=project, project_skills=project_skills, date=date)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def project_edit(id) -> Response or str:
    project = Project.query.get_or_404(id)
    date = project.date.strftime("%Y-%m")
    if request.form:
        new_date = datetime.datetime.strptime(request.form['date'], '%Y-%m')
        project.title = request.form['title']
        project.date = new_date
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projecteditform.html', project=project, date=date)


@app.route('/projects/<id>/delete')
def project_delete(id) -> Response:
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
