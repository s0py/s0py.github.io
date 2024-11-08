import os

# Set the paths to the two folders
md_folder = 'md'
html_folder = 'w'

def md_to_html(md_file, check_unique=True):
    print(f"Converting {md_file} to HTML...")

    # Read the Markdown file
    with open(os.path.join(md_folder, md_file), 'r') as f:
        md_content = f.read()

    # Convert Markdown to HTML
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
                <a class="a_nav" href="Azios.html">World Map</a>
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

    lines = md_content.split('\n')
    for line in lines:
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
                # Link as usual if the HTML file exists
                html_line = html_line[:start] + f'<a href="{link_text}.html">{link_text}</a>' + html_line[end+2:]
            else:
                # Change link text color to red if the file doesn't exist
                html_line = html_line[:start] + f'<a href="{link_text}.html" style="color: #ff0000;">{link_text}</a>' + html_line[end+2:]
        while '[' in html_line and '(' in html_line:
            start = html_line.index('[')
            end_link = html_line.index(')')
            end_text = html_line.index(']')
            link_text = html_line[start+1:end_text]
            link_url = html_line[end_text+2:end_link]
            html_line = html_line[:start] + f'<a href="{link_url}">{link_text}</a>' + html_line[end_link+1:]
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

# Loop through the Markdown files and convert them to HTML
def convert_all_md_to_html(check_unique=True):
    if check_unique:
        # Get a list of all files in the md folder
        md_files = [f for f in os.listdir(md_folder) if f.endswith('.md')]

        # Get a list of all files in the html folder
        html_files = [f[:-3] + '.html' for f in os.listdir(html_folder)]

        # Find the files in the md folder that are not in the html folder
        unique_md_files = [f for f in md_files if f[:-3] not in html_files]

        for md_file in unique_md_files:
            md_to_html(md_file)
    else:
        # Convert all Markdown files to HTML
        for md_file in os.listdir(md_folder):
            if md_file.endswith('.md'):
                md_to_html(md_file, check_unique=False)

# Convert all Markdown files to HTML, checking for unique files
convert_all_md_to_html(check_unique=False)

# Convert all Markdown files to HTML, without checking for unique files
# convert_all_md_to_html(check_unique=False)