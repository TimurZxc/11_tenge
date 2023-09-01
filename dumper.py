import os
import sys
import django
import json

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

# Initialize Django
django.setup()

# Now you can import your models and use Django functionality
from django.core.management import call_command

# Define the output JSON file path
output_file = 'data.json'

# Execute the dumpdata command and capture the output
with open(output_file, 'w', encoding='utf-8') as json_file:
    call_command('dumpdata', stdout=json_file, indent=2)

print(f'Data dumped to {output_file}')
