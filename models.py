from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column('Date', db.DateTime, default=datetime.now)
    title = db.Column('Title', db.String())
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills Practiced', db.Text)
    url = db.Column('Github URL', db.String())

    def __repr__(self):
        return f'''
        <Project (
            Title: {self.title}
            Description: {self.description}
            Skills Practiced: {self.skills}
            Github URL: {self.url}
            Date: {self.date}
        )'''
