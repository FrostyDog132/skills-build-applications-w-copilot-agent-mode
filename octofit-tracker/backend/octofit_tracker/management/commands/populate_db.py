from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB directly for index creation
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')

        # Activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user='Captain America', type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user='Batman', type='swim', duration=25, date='2024-01-03')
        Activity.objects.create(user='Superman', type='fly', duration=60, date='2024-01-04')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=85)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Sprint 100m 5 times', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank for 2 minutes', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
