from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Models here
class TitleModel(db.Model):
    __tablename__ = 'Title'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Integer, nullable=True)
    end_date = db.Column(db.Integer, nullable=True)
    chapter_count = db.Column(db.Integer, nullable=True)
    volume_count = db.Column(db.Integer, nullable=True)
