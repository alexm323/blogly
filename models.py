"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
import datetime

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    # we are going to set the table name , users is the logical choice here.
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
    posts = db.relationship('Post', backref='user',
                            cascade="all, delete-orphan")
# End of Columns.


class Post(db.Model):
    # we are going to set the table name , posts is the logical choice here.
    __tablename__ = 'posts'

    def __repr__(self):
        p = self
        return f"<Post id={p.id}, post_title = {p.title}, post_content = {p.content}, post_created_at = {p.created_at}>"

# Setting the columns
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    # created_at = db.Column(
    #     db.String(250), default=f'{datetime.now()}')

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now())

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class PostTag(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)


class Tag(db.Model):
    __tablename__ = 'tags'

    # def __repr__(self):
    #     t = self
    #     return f"<Tag Name = {t.name}, Tag ID = {t.id}"

    # set the columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)

    posts = db.relationship('Post', secondary='posts_tags',
                            cascade="all,delete", backref='tags')


# End of Columns
