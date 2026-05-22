import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Task 4: Replace orcid.png
    content = content.replace('orcid.png', 'orcid.svg')
    
    # Task 1: index.html stats strip removal
    if file == 'index.html':
        pattern = r'<div class="stats-strip">.*?</div>'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
    # Task 2 & 3: contact.html banner removal and form compaction
    if file == 'contact.html':
        # Removing Postdoc Banner
        banner_pattern = r'<div class="container">\s*<div style="background: var\(--navy\); color: #fff; padding: 1\.5rem; border-radius: var\(--radius\); text-align: center; margin-bottom: 2rem; box-shadow: var\(--shadow-soft\);">\s*<h3 style="color: #fff; margin:0;">Open to postdoctoral opportunities in Europe</h3>\s*<p style="margin: 0\.5rem 0 0; color: var\(--gold-soft\);">Available for positions starting Fall 2026</p>\s*</div>\s*</div>'
        content = re.sub(banner_pattern, '', content, flags=re.DOTALL)
        
        # Compact form
        content = content.replace('rows="6"', 'rows="3"')
        content = content.replace('<article class="card full-span">', '<article class="card full-span" style="padding: 1.5rem; max-width: 600px; margin: 0 auto;">')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Changes applied cleanly.")
