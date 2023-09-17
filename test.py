import os

def create_html_files_with_links(folder_path):
    if os.path.isdir(folder_path):
        folder_name = os.path.basename(folder_path)
        
        with open(f"{folder_name}.html", "w", encoding="utf-8") as html_file:
            html_file.write("{% extends 'docs.html' %}\n{% block links %}\n")
            items = os.listdir(folder_path)
            items.sort(key=lambda x: os.path.isdir(os.path.join(folder_path, x)), reverse=True)
            for item in items:
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    html_file.write("<tr>\n    <td colspan='3'>\n        <a href=\"{% url '"+item+"_url' %}\">"+item+"</a>\n    </td>\n</tr>")
                    create_html_files_with_links(item_path)
            
            html_file.write("{% endblock %}")
    else:
        print("The provided path is not a directory.")

your_folder_path = 'media/pdf/1-block'
create_html_files_with_links(your_folder_path)

