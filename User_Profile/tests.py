from django.test import TestCase
from User_Profile.models import Skills, Desires
# Create your tests here.
class SkillsTestCase(TestCase):
    def setUp(self):
	    self.skill1 = Skills.objects.create(skill="running", yearxp="10", description="I have run 10 marathons back to back.")
	
	def test_skills(self):
	    runner = Skills.objects.get(skill="running")
		self.assertEquals(runner.skill,"running")
		self.skill1.skill = "swimming"
		
		self.assertNotEquals(self.skill1.skill,"running")
		self.assertEquals(self.skill1.skill,"swimming")
		
class DesiresTestCase(TestCase):
    def setUp(self):
	    self.desires1 = Desires.objects.create(wants="food", description="I am hungry.")
	
	def test_desires(self):
	    foodie = Desires.objects.get(wants="food")
		self.assertEquals(foodie.wants,"food")
		self.desires1.wants = "sleep"
		
		self.assertNotEquals(self.desires1.wants,"food")
		self.assertEquals(self.desires1.wants,"sleep")