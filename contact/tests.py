from django.test import TestCase
from Contact.models import ContactForm

class ContactFormTestCase(TestCase):
    def setUp(self):
	    self.testingcase = ContactForm.objects.create(name="Bob" email="abcd@a.c" topic="ask you")
	
	def test_ContactForm(self):
	    contact = ContactForm.objects.get(name="Bob")
		self.assertEquals(contact.name,"Bob")
		self.testingcase.name = "Husk"
		
		self.assertNotEquals(self.testingcase.name,"Bob")
		self.assertEquals(self.testingcase.name,"Husk")