from django.conf import settings
import os
import io
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()

from app.models import File
from django.urls import path
from django.template import Template, Context

pdf_folder = 'media/pdf'
default_tag = ''
default_year = '2020-2021'
default_block = 2
html_content = ''


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

            # Generate URL pattern and HTML file
            folder_name = os.path.basename(os.path.dirname(relative_path))
            url_pattern = f"docs{relative_path}"
            html_content = "{"+f"% extends 'docs.html' %"+"}\n{" f"% block links %"+"}\n"
            for dirpath, dirnames, filenames in os.walk(os.path.join(pdf_folder, folder_name)):
                print('start')
                for dir in dirnames:
                    child_folder_name = dir
                    url_name = f"{child_folder_name}_url"
                    url_pattern = f"docs/{folder_name}/{child_folder_name}"
                    html_content += f"""
<tr>
    <td colspan="3"><a href="{{% url '{url_name}' %}}">{child_folder_name}</a></td>
</tr>
"""
                    # Add the URL pattern to your app's urls.py
                    with io.open('app/urls.py', 'a', encoding='utf-8') as urls_file:
                        urls_file.write(
                            f"path('{url_pattern}', Docs.as_view(template_name='{child_folder_name}.html', tag='{child_folder_name}'), name='{url_name}'),\n")

        html_content += "{% endblock %}"
        # Generate and save the HTML file
        html_file_name = os.path.join('templates', f'{folder_name}.html')
        with io.open(html_file_name, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

print("Files added to the database, URL patterns added to app/urls.py, and HTML files generated successfully.")