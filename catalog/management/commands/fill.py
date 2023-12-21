from django.core.management import BaseCommand

from catalog.models import Feedback


class Command(BaseCommand):

    def handle(self, *args, **options):
        feedback_list = [
            {'name': 'Anna', 'email': 'anna@gmail.com'},
            {'name': 'Bob', 'email': 'bob@gmail.com'},
            {'name': 'Cerol', 'email': 'cerol@gmail.com'},
            {'name': 'Diana', 'email': 'diana@gmail.com'},
            {'name': 'Igor', 'email': 'igor@gmail.com'},
            {'name': 'Frosya', 'email': 'frosya@gmail.com'},
            {'name': 'God', 'email': 'god@gmail.com'}
        ]

#        for feedback_item in feedback_list:
#            Feedback.objects.create(**feedback_item)

        feedback_for_create = []
        for feedback_item in feedback_list:
            feedback_for_create.append(
                Feedback(**feedback_item)
            )

#        print(feedback_for_create)
        Feedback.objects.bulk_create(feedback_for_create)
