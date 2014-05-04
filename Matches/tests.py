from django.test import TestCase
from Matches.models import Matches
from django.contrib.auth.models import User

# Create your tests here.
class MatchesTestCase(TestCase):
    def setUp(self):
        Joe=User.objects.create_user(username='joe',password='dlds')
        Catherine=User.objects.create_superuser(username='cathy', email='cats', password='cats')
        Joe =Matches.objects.create(user1 =Joe,user2=Catherine, offering='golf',recieving='soccer')
    def test_giving(self):
        Joe =Matches.objects.get(id=1)
        self.assertEqual(Joe.giving(),'golf')
    def test_recieved(self):
        John =Matches.objects.get(id=1)
        self.assertEqual(John.recieved(),'soccer')

            
            