from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.briana = User(username = 'briana',email = 'Briana@gmail.com')
        self.briana = Profile(user = self.briana,bio = 'tests',image = 'test.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.Briana,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    

class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',image = 'test.jpg',description = 'testD',link = 'https://test.com',created_date='Jan,25.2021')


    def test_save_project(self):
        self.new_post.save_project()
        image = Image.objects.all()
        self.assertEqual(len(image),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        image = Projects.objects.all()
        self.assertEqual(len(image),1) 

