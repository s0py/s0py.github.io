import os
from bs4 import BeautifulSoup

# Folder containing HTML files
folder_path = 'w'

# List to store missing files in the desired format
missing_files = []

# Loop through all HTML files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(file, 'html.parser')

            # Loop through all <a> elements
            for a_tag in soup.find_all('a'):
                href = a_tag.get('href')

                if href and href.endswith(".html"):
                    # Check if the target file exists
                    target_file_path = os.path.join(folder_path, href)

                    if not os.path.exists(target_file_path):
                        # If the file doesn't exist, remove the .html and format it
                        file_name = os.path.splitext(href)[0]
                        missing_files.append(f"[[{file_name}]]")

                        # Modify the style of the <a> element
                        a_tag['style'] = 'color: #ff0000'

            # Save the modified HTML back to the file
            with open(file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(str(soup))

# Specify the path to save the markdown file
output_folder = 'md'
output_file_path = os.path.join(output_folder, 'pages.md')

# only get unique
missing_files = list(set(missing_files))


# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Save the content to pages.md
with open(output_file_path, 'a') as dead_links_file:
    # Write the title at the beginning
    dead_links_file.write("\n# Dead Links\n")
    
    # Write each missing file in the desired format
    for missing_file in missing_files:
        dead_links_file.write(missing_file + '\n')

print("Dead links have been processed and appended to 'pages.md'.")
