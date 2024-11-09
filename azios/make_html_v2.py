import os

# Set the paths to the two folders
md_folder = 'md'
html_folder = 'w'

def process_markdown_line(line):
    """Helper function to process markdown in a single line"""
    html_line = line
    while '**' in html_line:
        start = html_line.index('**')
        end = html_line.index('**', start + 2)
        html_line = html_line[:start] + f'<b>{html_line[start+2:end]}</b>' + html_line[end+2:]
    while '*' in html_line:
        start = html_line.index('*')
        end = html_line.index('*', start + 1)
        html_line = html_line[:start] + f'<i>{html_line[start+1:end]}</i>' + html_line[end+1:]
    while '[[' in html_line:
        start = html_line.index('[[')
        end = html_line.index(']]', start)
        link_text = html_line[start+2:end]
        
        # Check if the corresponding HTML file exists
        html_file_path = os.path.join(html_folder, f"{link_text}.html")
        if os.path.exists(html_file_path):
            html_line = html_line[:start] + f'<a href="{link_text}.html">{link_text}</a>' + html_line[end+2:]
        else:
            html_line = html_line[:start] + f'<a href="{link_text}.html" style="color: #ff0000;">{link_text}</a>' + html_line[end+2:]
    return html_line

def md_to_html(md_file, check_unique=True):
    print(f"Converting {md_file} to HTML...")

    # Read the Markdown file
    with open(os.path.join(md_folder, md_file), 'r') as f:
        md_content = f.read()

    # Basic HTML template (truncated for brevity)
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{}</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #000000;
                color: #DAE0F2;
                background-image:url('starry.webp');
                background-repeat:repeat;
            }}
            .container {{
                background-color: #1a1d22;
                border-left: 1px solid #F9CFF2;
                border-right: 1px solid #F9CFF2;
                margin: 0% 9% 0% 3%;
                padding: 1% 6% 2.5% 6%;
                box-shadow: 10px 0 15px -10px #97a09f, 
                           -10px 0 15px -10px #97a09f;
                line-height: 24px;
                font-size: 14px;
                font-family: Roboto;
                font-weight: 400;
                letter-spacing: .03125em;
            }}
            .container-banner {{
                text-align: center;
                background-color: #232b33;
                border-bottom: 1px solid #F9CFF2;
                padding: 1em;
                margin: 1em 0em;
                font-size:12px;
                line-height: 16px;
                display: grid; 
                grid-template-columns: minmax(50px, 100px) 1fr minmax(50px, 100px); 
                gap: 0px;
            }}
            a {{
                color: #6fbce8;
                font-weight: 400;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
                text-decoration-style: dotted;
                color: #F9CFF2;
            }}
            h1, h2, h3, h4 {{
                font-family: 'Times New Roman', Georgia, Times, serif;
                font-weight: bold;
                color: #ffffff;
                border-bottom: 1px solid #FFFFFF;
                padding: 5px 0px;
                margin-top: 0em;
                margin-bottom: 0.5em;
            }}
            b {{
                font-weight: 800;
            }}
            .nav {{
                text-align: left;
                padding: 1em 2em 1em 2em;
                margin: 0em 0em 0em 1em;
                background-color: rgba(26,29,34,0.5);
                font-family: Roboto;
                width: 10%;
                line-height: 24px;
                min-width: 100px;
            }}
            .a_nav {{
                color: #ffffff;
                font-size: 12px;
            }}
            .a_nav:hover {{
                color: #F9CFF2;
                text-decoration: underline;
            }}
            .row {{
                display: flex;
            }}
        </style>
    </head>
    <body>
        <div class="row">
            <div class="nav">
                <a class="a_nav" href="pages.html">All Pages</a><br style="line-height: 0px">
                <hr style="border: none; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.33), transparent); margin-bottom:1em;">
                <a class="a_nav" href="Azios.html">World Map</a><br style="line-height: 0px">
                <a class="a_nav" href="Cosmology.html">Cosmology</a>
                <hr style="border: none; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.33), transparent); margin-bottom:1em;">
                <h4>Categories</h4>
                <a class="a_nav" href="Peoples.html">Peoples</a><br style="line-height: 0px">
                <a class="a_nav" href="Magic.html">Magic</a><br style="line-height: 0px">
                <a class="a_nav" href="Locations.html">Locations</a><br style="line-height: 0px">
                <hr style="border: none; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.33), transparent); margin-bottom:1em;">
                <h4>Regions</h4>
                <a class="a_nav" href="Ashen Empire.html">Ashen Empire</a><br style="line-height: 0px">
                <a class="a_nav" href="Crifico.html">Crifico</a><br style="line-height: 0px">
                <a class="a_nav" href="Ethqmir.html">Ethqmir</a><br style="line-height: 0px">
                <a class="a_nav" href="Far Lands.html">Far Lands</a><br style="line-height: 0px">
                <a class="a_nav" href="Featherscale Isles.html">Featherscale Isles</a><br style="line-height: 0px">
                <a class="a_nav" href="Four Cities.html">Four Cities</a><br style="line-height: 0px">
                <a class="a_nav" href="Gangling Grove.html">Gangling Grove</a><br style="line-height: 0px">
                <a class="a_nav" href="Goolands.html">Goolands</a><br style="line-height: 0px">
                <a class="a_nav" href="Qthemir.html">Qthemir</a><br style="line-height: 0px">
                <a class="a_nav" href="Salt and Silence.html">Salt & Silence</a><br style="line-height: 0px">
                <a class="a_nav" href="Serica.html">Serica</a><br style="line-height: 0px">
                <a class="a_nav" href="Skittering Wilder.html">Skittering Wilder</a><br style="line-height: 0px">
                <a class="a_nav" href="Tea Lands.html">Tea Lands</a><br style="line-height: 0px">
                <a class="a_nav" href="Ulaan.html">Ulaan</a><br style="line-height: 0px">
                <a class="a_nav" href="United Baronies.html">United Baronies</a><br style="line-height: 0px">
                <a class="a_nav" href="Xibalba.html">Xibalba</a><br style="line-height: 0px">
                <a class="a_nav" href="Yartzland.html">Yartzland</a><br style="line-height: 0px">
                <hr style="border: none; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.33), transparent); margin-bottom:1em;">
                <h4>Popular</h4>
                <a class="a_nav" href="Vichmeister.html">Vichmeister</a><br style="line-height: 0px">
            </div>
        <div class="container">
        <div class="container-banner">
            <div>
                <img src="flower-kid.png" alt="Flower Kid" style="max-width: 8em; height: auto;">
            </div>
            <div>
                <b>Welcome to Azios!</b>
                <br>
                "The World of the Morning Star"
                <br>
                <br>
                This is a wiki for a personal worldbuilding project.
                <p style="font-size:8px;">CC BY-NC-SA</p>
            </div>
            <div>
                <img src="three-kings.png" alt="Three Kings" style="max-width: 8em; height: auto;">
            </div>
        </div>

    """.format(md_file[:-3])


    # Import re for easier text searching and processing
    import re
    
    lines = md_content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        html_line = line
        
        # Handle images and standard links separately
        while '[' in html_line and '(' in html_line:
            start = html_line.index('[')
            end_link = html_line.index(')')
            end_text = html_line.index(']')
        
            # Extract the text and URL
            link_text = html_line[start + 1:end_text]
            link_url = html_line[end_text + 2:end_link]
        
            if html_line[start - 1] == '!':  # Check if it's an image
                # Collect and process text until the next heading
                processed_text = ""
                j = i + 1
                while j < len(lines):
                    if re.match(r'^(#{1,4} )', lines[j]):  # Check if the line is a heading
                        break
                    # Process markdown in the text alongside the image
                    processed_line = process_markdown_line(lines[j])
                    processed_text += processed_line + "<br>"
                    j += 1
                i = j - 1  # Update main loop counter to skip processed lines
        
                # Generate HTML for the image with processed text
                html_line = (
                    html_line[:start - 1] +
                    f'<div style="display: flex;">'
                    f'<div style="flex-grow: 1; margin-right: 2em;">{processed_text}</div>'
                    f'<div style="max-width: 300px; margin-left: auto; align-self: flex-start;">'
                    f'<div style="text-align: center; border: 1px solid #F9CFF2; padding: 0.5em;">'
                    f'<img src="{link_url}" alt="{link_text}" style="width: 100%; height: auto;">'
                    f'<div style="font-size: 14px; color: #AAB0C2; margin-top: 5px;">{link_text}</div>'
                    f'</div></div></div>'
                )
            else:
                # Standard link processing
                html_line = (
                    html_line[:start] + 
                    f'<a href="{link_url}">{link_text}</a>' + 
                    html_line[end_link + 1:]
                )
        
        # Process remaining markdown in the line
        html_line = process_markdown_line(html_line)
        
        # Handle headers
        if html_line.startswith('# '):
            html_content += f'<h1>{html_line[2:]}</h1>\n'
        elif html_line.startswith('## '):
            html_content += f'<h2>{html_line[3:]}</h2>\n'
        elif html_line.startswith('### '):
            html_content += f'<h3>{html_line[4:]}</h3>\n'
        elif html_line.startswith('#### '):
            html_content += f'<h4>{html_line[5:]}</h4>\n'
        else:
            html_content += f'{html_line}<br>\n'
        
        i += 1

    # Close HTML
    html_content += f"""
        <br>
        <div style="text-align: center; margin-top: 20px;">
            <hr style="border: none; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.33), transparent); margin-bottom:1em;">
            Original File: <a href="../{md_folder}/{md_file}">
                {md_file}
            </a>
        </div>
        </div>
        </body>
    </html>
    """

    # Save the HTML file
    html_file = md_file[:-3] + '.html'
    with open(os.path.join(html_folder, html_file), 'w') as f:
        f.write(html_content)

def convert_all_md_to_html(check_unique=True):
    if check_unique:
        # Get a list of all files in the md folder
        md_files = [f for f in os.listdir(md_folder) if f.endswith('.md')]

        # Find the files in the md folder that are not in the html folder
        html_files = [f[:-5] + '.html' for f in md_files]
        unique_md_files = [f for f in md_files if f[:-3] + '.html' not in os.listdir(html_folder)]

        for md_file in unique_md_files:
            md_to_html(md_file)
    else:
        # Convert all Markdown files to HTML
        for md_file in os.listdir(md_folder):
            if md_file.endswith('.md'):
                md_to_html(md_file, check_unique=False)

# Convert all Markdown files to HTML, checking for unique files
convert_all_md_to_html(check_unique=False)


# List to store the .html file names
html_files = []

# Walk through every file in the folder
for file_name in os.listdir(html_folder):
    if file_name.endswith('.html'):
        # Remove the .html extension and add to the list
        html_files.append(file_name[:-5])

# Prepare the content for the markdown file
markdown_content = "# All Pages\n"
for file_name in html_files:
    if file_name != "pages":
        if file_name != "dead_links":
            markdown_content += f"[[{file_name}]]\n"

# Specify the path to save the markdown file
output_folder = 'md'
output_file_path = os.path.join(output_folder, 'pages.md')

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Save the content to pages.md
with open(output_file_path, 'w') as file:
    file.write(markdown_content)

print("HTML file list saved to pages.md")



# dead link processing
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
missing_files.sort()


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
