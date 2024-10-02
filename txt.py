files = ["1.txt", "2.txt", "3.txt"]

file_data = []

def get_number_of_lines(file_info):
    return file_info[1]

for file in files:
    with open(file, 'r', encoding = 'utf-8') as f:
        file_content = f.read()
        file_lines = file_content.split('\n')
        file_data.append((file, len(file_lines), file_content))

def merge_files(file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])

    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for file_name, line_count in sorted_file_data:
            file_content = open(file_name, encoding='utf-8').read()
            result_file.write(f'Имя файла: {file_name}\\n')
            result_file.write(f'Количество строк: {line_count}\\n')
            result_file.write(file_content + '\\n\\n')

with open("4.txt", 'w', encoding = 'utf-8') as result_file:
    for file_info in sorted_file_data:
        result_file.write(f"{file_info[0]}\n{file_info[1]}\n{file_info[2]}\n\n")

