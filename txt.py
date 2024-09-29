files = ["1.txt", "2.txt", "3.txt"]

file_data = []

def get_number_of_lines(file_info):
    return file_info[1]

for file in files:
    with open(file, 'r', encoding = 'utf-8') as f:
        file_content = f.read()
        file_lines = file_content.split('\n')
        file_data.append((file, len(file_lines), file_content))

sorted_file_data = sorted(file_data, key=get_number_of_lines)

with open("4.txt", 'w', encoding = 'utf-8') as result_file:
    for file_info in sorted_file_data:
        result_file.write(f"{file_info[0]}\n{file_info[1]}\n{file_info[2]}\n\n")