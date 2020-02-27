from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTest(TestCase):
    def setUp(seft):
        Post.objects.create(
            title='myTitle',
            body='just a Test'
        )
    def test_string_representation(self):
        post = Post(title='My entry title')
        self.assertEqual(str(post), post.title)
    def test_post_list_view(self):
        respone = self.client.get('/blog/')
        self.assertEqual(respone.status_code, 200)
        self.assertContains(respone,'myTitle')
        self.assertTemplatesUsed(respone, 'blog/blog.html')
    def test_post_detail_views(self):
        respone = self.client.get('/blog/1/')
        self.assertEqual(respone.status_code, 200)
        self.assertContains(respone,'myTitle')
        self.assertTemplatesUsed(respone, 'blog/post.html')
