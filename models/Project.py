from .database import db
import datetime


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    link = db.Column('Link', db.Text)

    def __repr__(self):
        return f'''<Project (Title: {self.title}
                             Date: {self.date}
                             Description: {self.description}
                             Skills: {self.skills}
                             Link: {self.link})>'''
