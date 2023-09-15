from django.conf import settings
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()

from app.models import File
pdf_folder = 'media\pdf'
default_tag = 'common'
default_year = '2020-2021'
default_block = 2

for root, _, files in os.walk(pdf_folder):
    for filename in files:
        if filename.endswith('.pdf'):
            # Get the relative path from pdf_folder to the current file
            relative_path = os.path.relpath(os.path.join(root, filename), pdf_folder)
            
            # Extract the parts of the relative path
            path_parts = os.path.dirname(relative_path).split(os.path.sep)
            
            # Use the parts of the relative path to set tag and file
            tag = path_parts[-1]  # Use the directory structure as the tag
            if tag == ('' or None):
                tag = default_tag
            file_path = os.path.join('pdf', relative_path)  # Relative path to the PDF file
            
            # Check if the year is in the filename or use the default
            for year_choice, _ in File.year_choices:
                if year_choice in filename:
                    year = year_choice
                    break
            else:
                year = default_year
            
            # Create and save the File instance
            name = os.path.splitext(filename)[0]
            file_instance = File(
                name=name, file=file_path, tag=tag, year=year, block=default_block)
            file_instance.save()

print("Files added to the database successfully.")
