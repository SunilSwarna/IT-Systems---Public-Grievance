from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import resolve,reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.http import HttpRequest
from music.views import index, login1

class HomePageTest(TestCase):
    
    def setUp(self):
        self.c = Client()
        #Creating Dummy User
        self.user = User.objects.create(username='testuser')
        self.user.set_password('none')
        self.user.save()

    def test_existing_login(self):
    	#Checking Whether the Registerd user can login or not
        login = self.c.login(username='testuser',password='none')
        if login :
            self.c.logout()
        self.assertTrue(login)

    def test_non_existing_login(self):
        # If a user who is not existing tries to login 
        l_data = {'username':'fake', 'password':'pass'}
        login2 = self.c.post('/music/login1',data=l_data,follow=True)
        
        self.assertEqual(login2.status_code, 200)
    def test_exiting_user_wrong_password(self):
    	# Existing User tries to login with wrong password
    	l_data = {'username':'testuser', 'password':'password'}
        login3 = self.c.post('/music/login1',data=l_data,follow=True)
        
        self.assertEqual(login3.status_code, 200)
