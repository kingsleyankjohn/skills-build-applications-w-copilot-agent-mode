
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': marvel},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            user_objs.append(user)

        # Create activities
        Activity.objects.create(name='Running', user='ironman', team='Marvel')
        Activity.objects.create(name='Swimming', user='batman', team='DC')
        Activity.objects.create(name='Cycling', user='spiderman', team='Marvel')
        Activity.objects.create(name='Flying', user='superman', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='batman', team='DC', score=90)
        Leaderboard.objects.create(user='spiderman', team='Marvel', score=80)
        Leaderboard.objects.create(user='superman', team='DC', score=95)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', user='ironman')
        Workout.objects.create(name='Situps', description='Do 100 situps', user='batman')
        Workout.objects.create(name='Pullups', description='Do 20 pullups', user='spiderman')
        Workout.objects.create(name='Squats', description='Do 60 squats', user='superman')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
