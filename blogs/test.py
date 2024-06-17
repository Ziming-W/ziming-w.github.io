import re

# Function to replace \[n\] with [^n]
def replace_references(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Use regex to find and replace all occurrences of \[n\] with [^n]
    updated_content = re.sub(r'\\\[(\d+)]', r'[^\\1]', content)
    
    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

# Specify the path to your Markdown file
file_path = 'consensus-raft.md'

# Call the function to replace references
replace_references(file_path)