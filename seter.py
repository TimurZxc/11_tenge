import json
from app.models import File
import os
import django# Now you can import your Django models and use the settings
from app.models import File  # Replace 'your_app' with the actual name of your Django app
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")  # Replace with your actual project's settings module

# Manually configure Django settings
django.setup()



json_file_path = 'data.json'
def import_data(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        print(item)
        # my_model_instance = File(
        #     name=item['name'],
        #     description=item['description']
        # )
        # my_model_instance.save()

if __name__ == "__main__":
    json_file_path = "data.json"
    import_data(json_file_path)
