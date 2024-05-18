import re




def remove_text_after_double_dash(file_path):
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Process each line to remove text after '--'
    processed_lines = []
    for line in lines:
        if '--' in line :
            # Split the line at '--' and take the part before it
            processed_line = line.split('--')[0]
            if "'" in line:
                processed_line = processed_line + "'"
            processed_lines.append(processed_line + '\n')  # Add newline back to maintain line breaks
        else:
            processed_lines.append(line)

    # Step 3: Write the processed lines back to the file
    with open("output1.txt", 'w') as file:
        file.writelines(processed_lines)

# Example usage
file_path = 'query.txt'
remove_text_after_double_dash(file_path)



def replace_execute_immediate(file_path):
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Process each line to replace the specific line using regex
    new_lines = []
    pattern1 = re.compile(r'^.*execute\s+immediate\s+vquery\s*', re.IGNORECASE)
    pattern2 = re.compile(r'^.*execute\s+immediate\s+vbquery\s*', re.IGNORECASE)
    replacement1 = 'insert into zzvalue();\n'
    replacement2 = 'insert into zzvalue(2);\n'
    
    for line in lines:
        
        if pattern1.match(line):
            new_lines.append(replacement1)
        if pattern2.match(line):
            new_lines.append(replacement2)
       
        new_lines.append(line)
    
    # Step 3: Write the modified lines back to the file
    with open('output2.txt', 'w') as file:
        file.writelines(new_lines)

# Example usage
file_path = 'output1.txt'
replace_execute_immediate(file_path)




file_path = 'output2.txt'
old_text = 'hi0718001'
new_text = 'oe07718001'

# Read the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Replace old_text with new_text
file_content = re.sub(re.escape(old_text), new_text, file_content, flags=re.IGNORECASE)


# Write the updated content back to the file
with open('output3.txt', 'w') as file:
    file.write(file_content)

print(f'Replaced {old_text} with {new_text} in {file_path}.')

