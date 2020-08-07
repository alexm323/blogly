"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    # we are going to set the table name , pets is the logical choice here.
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id={u.id}, First_Name = {u.first_name}, Last_Name = {u.last_name}, image_url = {u.image_url}>"

# Setting the columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)

    image_url = db.Column(db.String(200), nullable=True,
                          default='https://t4.ftcdn.net/jpg/00/64/67/63/240_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg')

# End of Columns
