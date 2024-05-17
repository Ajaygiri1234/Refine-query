import re

def replace_execute_immediate(file_path):
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Process each line to replace the specific line using regex
    new_lines = []
    pattern = re.compile(r'^\s*execute\s+immediate\s+vquery\s*', re.IGNORECASE)
    replacement = 'insert into zzvalue();\n'
    
    for line in lines:
        
        if pattern.match(line):
            new_lines.append(replacement)
       
        new_lines.append(line)
    
    # Step 3: Write the modified lines back to the file
    with open('c.txt', 'w') as file:
        file.writelines(new_lines)

# Example usage
file_path = 'b.txt'
replace_execute_immediate(file_path)
