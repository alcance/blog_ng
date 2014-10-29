from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blogengine.models import Post
'''
Post model has:
- title
- a publication date an time
- some text
What would you like to test?
- set title
- set publication date and time
- set some text
- save it
- retrieve it
'''


class PostTest(TestCase):
    def test_create_post(self):
        # Create new post
        post = Post()
        # Set the attributes
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        # Save it
        post.save()
        """
        # Check we can retrieve it
        1. Fetch all objects
        2. assert that there is only 1 post object
        3. retrive that post object
        4. assert that it is the same object as the post object we just saved
        """
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Check attributes
        self.assertEquals(only_post.title, 'My first post'),
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, post.pub_date.second)


class AdminTest(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        # Create client
        self.client = Client()

    def test_login(self):
        # Get login page
        response = self.client.get('/admin/')

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

        # Log the user in
        self.client.login(username='dong', password="password")

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

    def test_logout(self):
        # Log in
        self.client.login(username='dong', password="password")

        # Check for reponse code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertTrue(response.status_code, 200)

        # Check 'Log in' in response
        response = self.client.get('/admin/')
        self.assertTrue('Log in' in response.content)
