from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post









class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls): # one time create data and every test can use it
        cls.user = User.objects.create(username='test1')
        cls.post1 = Post.objects.create(
            title='test1',
            text='test for post 1 :)))) ',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title='post2',
            text='raz is here',
            status=Post.STATUS_CHOICES[0][1],
            author=cls.user,
        )


    # def setUp(self): # every time for any unit test it create data
    #     self.user = User.objects.create(username='test1')
    #     self.post1 = Post.objects.create(
    #         title='test1',
    #         text='test for post 1 :)))) ',
    #         status=Post.STATUS_CHOICES[0][0],
    #         author=self.user,
    #     )
    #     self.post2 = Post.objects.create(
    #         title='post2',
    #         text='raz is here',
    #         status=Post.STATUS_CHOICES[0][1],
    #         author=self.user,
    #     )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'test1')
        self.assertEqual(self.post1.text, 'test for post 1 :)))) ')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_name_url(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response,'test1')

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_details_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_name_url(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_status_404_if_page_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_posts_are_not_post_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'this is test',
            'text': 'test text for text :D',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'this is test')
        self.assertEqual(Post.objects.last().text, 'test text for text :D')
         
    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'this is update',
            'text': 'test text for updateeee :D',
            'status': 'pub',
            'author': self.post2.author.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'this is update')
        self.assertEqual(Post.objects.last().text, 'test text for updateeee :D')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code,302)














