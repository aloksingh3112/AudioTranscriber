import os
import json
from api.models import CharacterSet
from django.core.management.base import BaseCommand
from transcribeAudio.settings import BASE_DIR


class Command(BaseCommand):
    def import_characterset_from_file(self):
        data_folder = os.path.join(
            BASE_DIR, 'api', 'resources/charactersets')

        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    id = data_object['id']
                    text = data_object['text']
                    try:
                        characterset, created = CharacterSet.objects.update_or_create(
                            id=id,
                            defaults={'text': text}
                        )
                        if created:
                            characterset.save()
                            display_format = "\n charaterset, {}, has been saved."
                            print(display_format.format(characterset))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this characterset: {}\n{}".format(
                            text, str(ex))
                        print(msg)

    def handle(self, *args, **options):

        self.import_characterset_from_file()
