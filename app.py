"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

# SQLA configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# End SQLA configurations
# Start Debug Toolbar
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
# End Debug Toolbar config

connect_db(app)
db.create_all()


@app.route('/')
def redirect_to_users():
    """Show list of all users"""

    return redirect('/users')

# List of users


@app.route('/users')
def list_users():
    """Show list of all users"""
    users = User.query.all()
    return render_template('users.html', users=users)
# End list of users route
# Create a new user route and logic


@app.route('/users/new')
def new_user_form():

    return render_template('new_user_form.html')


@app.route('/users/new', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    image_url = image_url if image_url else None
    new_user = User(first_name=first_name,
                    last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'{new_user.id}')
# New user logic ends

# User details Page


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)
# User details route ends
# Editing a user route and logic


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def save_edit(user_id):
    """Show details about a single pet"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    edit_user = User.query.get_or_404(user_id)

    edit_user.first_name = first_name
    edit_user.last_name = last_name
    edit_user.image_url = image_url

    db.session.commit()

    return redirect('/')


@app.route('/users/<int:user_id>/delete', methods=['GET', 'POST'])
def delete_user(user_id):
    """Show details about a single pet"""
    # delete_user = User.query.get_or_404(user_id)
    User.query.filter_by(id=user_id).delete()

    db.session.commit()

    return redirect('/')
# End editing route logic
