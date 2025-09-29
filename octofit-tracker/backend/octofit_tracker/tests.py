from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_activity(self):
        activity = Activity.objects.create(name='Test Activity', user='testuser', team='Test Team')
        self.assertEqual(activity.name, 'Test Activity')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user='testuser', team='Test Team', score=10)
        self.assertEqual(leaderboard.score, 10)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', user='testuser')
        self.assertEqual(workout.name, 'Test Workout')
