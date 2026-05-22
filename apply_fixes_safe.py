import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Task 2: index.html stats strip removal
    if file == 'index.html':
        pattern = r'<section class="section pub-stats".*?</section>'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
    # Task 3: Replace Chemistry-A European Journal
    content = re.sub(r'Chemistry[-—]A European Journal', 'Chemistry &ndash; A European Journal', content)
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Changes applied safely.")
