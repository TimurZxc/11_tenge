import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")  # Replace with your actual project's settings module

# Manually configure Django settings
django.setup()

# Now you can import your Django models and use the settings
from app.models import File  # Replace 'your_app' with the actual name of your Django app
from django.conf import settings

# Define the folder path where your PDF files are located
pdf_folder = os.path.join(settings.MEDIA_ROOT,'pdf_block1')  # Replace with the actual path

# Define default values
default_tag = 'common'
default_year = '2020-2021'
default_block = 1

# Iterate through the files in the folder
for filename in os.listdir(pdf_folder):
    if filename:
        # Extract the name without the file extension
        name = os.path.splitext(filename)[0]

        # Check if the year is present in the filename
        for year_choice, year_label in File.year_choices:
            if year_choice in name:
                year = year_choice
                break
        else:
            year = default_year

        # Create a File object and save it to the database
        file_instance = File(name=name, file=os.path.join('pdf_block1', filename), tag=default_tag, year=year, block=default_block)
        file_instance.save()

print("Files added to the database successfully.")

