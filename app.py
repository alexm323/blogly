"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import *
from datetime import datetime

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
    posts = Post.query.filter_by(user_id=user_id)
    return render_template('details.html', user=user, posts=posts)
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

# Show the details of a post logic


@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    """Show the details of a post"""

    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()

    return render_template('post_details.html', post=post, tags=tags)

    # end show post logic

# posting something new logic


@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('new_post_form.html', user=user, tags=tags)


@app.route('/users/<int:user_id>/posts/new', methods=['GET', 'POST'])
def new_post_submit(user_id):
    user = User.query.get_or_404(user_id)
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    new_post = Post(title=request.form['title'],
                    content=request.form['content'],
                    user=user,
                    tags=tags)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')
# end of making a new post

# Begin Edit to post


@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show details about a single pet"""
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('edit_post.html', post=post, tags=tags)


@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post_submit(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(post)

    db.session.commit()
    return redirect(f'/posts/{post_id}')
# End Edit of post

# Start of post deletion logic


@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    """Delete post"""
    delete_post = Post.query.get_or_404(post_id)
    Post.query.filter_by(id=post_id).delete()

    db.session.commit()
    return redirect('/')
# End of deletion of post


# Tags section start
@app.route('/tags')
def show_all_tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)


@app.route('/tags/<int:tag_id>')
def show_tag(tag_id):
    '''Show details and posts with a single tag'''
    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()

    return render_template('tag_details.html', tag=tag, posts=posts)


@app.route('/tags/new')
def new_tag_form():
    return render_template('add_tag.html')


@app.route('/tags/new', methods=['GET', 'POST'])
def new_tag_submit():
    tag_name = request.form['tag']
    new_tag = Tag(name=tag_name)

    db.session.add(new_tag)
    db.session.commit()
    return redirect(f'/tags')


@app.route('/tags/<int:tag_id>/edit')
def edit_tag_form(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('edit_tag.html', tag=tag)


@app.route('/tags/<int:tag_id>/edit', methods=['GET', 'POST'])
def edit_tag_submit(tag_id):
    edited_tag_name = request.form['tag_name']
    revised_tag = Tag.query.get_or_404(tag_id)
    revised_tag.name = edited_tag_name
    db.session.commit()
    return redirect(f'/tags')


@app.route('/tags/<int:tag_id>/delete')
def delete_tag(tag_id):
    delete_tag = Tag.query.get_or_404(tag_id)
    Tag.query.filter_by(id=tag_id).delete()

    db.session.commit()
    return redirect(f'/tags')
# Tags section end

# # Start of post deletion logic

# cant delete posts now -_-
