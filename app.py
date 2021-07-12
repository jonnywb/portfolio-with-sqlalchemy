from flask import (render_template, url_for,
                   request, redirect)
from models import db, Project, app
import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


def clean_date(date_str):
    split_date = date_str.split('-')

    month = int(split_date[1])
    year = int(split_date[0])

    return datetime.date(year, month, 1)


@app.route('/projects/new', methods=['GET', 'POST'])
def create():
    projects = Project.query.all()
    if request.form:
        new_project = Project(
            date=clean_date(request.form['date']),
            title=request.form['title'],
            description=request.form['desc'],
            skills=request.form['skills'],
            url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addproject.html', projects=projects)


@app.route('/projects/<id>')
def detail(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    date_str = project.date.strftime("%B %Y")
    return render_template('detail.html', project=project,
                           date=date_str, projects=projects)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    date = project.date.strftime("%Y-%m")
    if request.form:
        project.date = clean_date(request.form['date'])
        project.title = request.form['title']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project,
                           date=date, projects=projects)


@app.route('/projects/<id>/delete')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', projects=projects,
                           msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
