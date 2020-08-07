from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class BloglyViewsTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample User."""

        User.query.delete()

        user = User(first_name='Alexander', last_name='Hamilton',
                    image_url='https://upload.wikimedia.org/wikipedia/commons/0/05/Alexander_Hamilton_portrait_by_John_Trumbull_1806.jpg')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Alexander', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Alexander Hamilton</h1>', html)

    def test_new_user_form(self):
        with app.test_client() as client:
            resp = client.get(f'/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('First Name', html)
            self.assertIn('Last Name', html)
            self.assertIn('Image URL', html)

    def test_create_user(self):
        with app.test_client() as client:
            d = {"first_name": "Aaron", "last_name": "Burr",
                 "image_url": 'http://www.broken.jpeg'}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Aaron Burr</h1>", html)
