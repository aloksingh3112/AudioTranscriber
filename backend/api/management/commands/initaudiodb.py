import os
import json
from api.models import Audio
from django.core.management.base import BaseCommand
from transcribeAudio.settings import BASE_DIR


class Command(BaseCommand):
    def import_audio_from_file(self):
        data_folder = os.path.join(
            BASE_DIR, 'api', 'resources/audios')
        print(data_folder)

        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    id = data_object.get('id', None),
                    title = data_object.get('title', None)
                    audioLink = data_object.get('audioLink', None)
                    try:
                        audio, created = Audio.objects.update_or_create(
                            id=id,
                            defaults={
                                'title': title,
                                'audioLink': audioLink,
                            }

                        )
                        if created:
                            audio.save()
                            display_format = "\nAudio, {}, has been saved."
                            print(display_format.format(audio))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this audio: {}\n{}".format(
                            title, str(ex))
                        print(msg)

    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_audio_from_file()
