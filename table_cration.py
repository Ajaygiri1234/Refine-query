import re 



def get_words_starting_with_hi0718001(file_path):
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Initialize an empty list to store the matched words
    matched_words = []
    
    # Step 3: Define the regex pattern to match words starting with 'hi0718001'
    pattern = re.compile(r'\bhi0718001.\w*\b', re.IGNORECASE)
    
    # Step 4: Search for the pattern in each line
    for line in lines:
        matches = pattern.findall(line)
        matched_words.extend(matches)
    
    return matched_words

# Example usage
file_path = 'query.txt'
hi_table_list = get_words_starting_with_hi0718001(file_path)
for table in hi_table_list:
    print(table)




hi_table_list = ['a', 'b', 'c']
source_table = 'hi0718001'

# Initialize an empty list to store the formatted strings
create_table_queries = []

# Generate the create table queries for each table name
for table_name in table_names:
    query = f"create table {table_name} as select * from {source_table}.{table_name} where 1=2"
    create_table_queries.append(query)

# Join the queries into a single string
combined_query = ';\n'.join(create_table_queries)

print(combined_query)
with open("table_creation_query", 'w') as file:
    file.write(combined_query)


