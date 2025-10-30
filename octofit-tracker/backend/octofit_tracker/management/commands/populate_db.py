
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

        # Create users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='password')
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='password')
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='password')
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='password')

        # Create activities
        Activity.objects.create(user='tony', type='run', duration=30, team='Marvel')
        Activity.objects.create(user='bruce', type='swim', duration=45, team='Marvel')
        Activity.objects.create(user='clark', type='fly', duration=60, team='DC')
        Activity.objects.create(user='diana', type='jump', duration=50, team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
