from django.conf import settings
import os
import io
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()

from app.models import File
from django.urls import path
from django.template import Template, Context

pdf_folder = 'media/pdf/1-block'
default_tag = ''
default_year = '2020-2021'
default_block = 1
html_content = ''



for root, _, files in os.walk(pdf_folder):
    for filename in files:
        if True:
            relative_path = os.path.relpath(os.path.join(root, filename), pdf_folder)
            path_parts = os.path.dirname(relative_path).split(os.path.sep)
            tag = path_parts[-1]  # Use the directory structure as the tag
            if tag == ('' or None):
                tag = default_tag
            file_path = os.path.join('pdf', relative_path)  # Relative path to the PDF file
            for year_choice, _ in File.year_choices:
                if year_choice in filename:
                    year = year_choice
                    break
            else:
                year = default_year
            
            name = os.path.splitext(filename)[0]
            file_instance = File(
                name=name, file=file_path, tag=tag, year=year, block=default_block)
            file_instance.save()

            # Generate URL pattern and HTML file
            folder_name = os.path.basename(os.path.dirname(relative_path))
            url_pattern = f"docs{relative_path}"
            for dirpath, dirnames, filenames in os.walk(os.path.join(pdf_folder, folder_name)):
                for dir in dirnames:
                    child_folder_name = dir
                    url_name = f"{child_folder_name}_url"
                    url_pattern = f"docs/1-block/{folder_name}/{child_folder_name}"
                    with io.open('app/urls.py', 'a', encoding='utf-8') as urls_file:
                        urls_file.write(
                        f"path('{url_pattern}', Docs.as_view(template_name='{child_folder_name}.html', tag='{child_folder_name}', block=1), name='{url_name}'),\n")##



print("Files added to the database, URL patterns added to app/urls.py, and HTML files generated successfully.")
