"""Seed file to make sample data for pets db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets

ben = User(first_name='Benjamin', last_name="Franklin",
           image_url='https://images.unsplash.com/photo-1493612276216-ee3925520721?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80')
alexander = User(first_name='Alexander', last_name="Hamilton",
                 image_url='https://images.unsplash.com/photo-1514580426463-fd77dc4d0672?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60')
thomas = User(first_name='Thomas', last_name="Paine",
              image_url='https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60')

# Add new objects to session, so they'll persist
db.session.add(ben)
db.session.add(alexander)
db.session.add(thomas)

# Commit--otherwise, this never gets saved!
db.session.commit()
