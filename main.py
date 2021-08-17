def files_sort(files):
    
    all_files = {}
    all_files_sorted = {}

    for file in files:
        with open(file) as f:
            lines = f.read()
            all_files[len(lines.split('\n'))] = {file: lines}

    all_files = sorted(all_files.items())

    for el in all_files:
        all_files_sorted[el[0]] = el[1]

    with open('result.txt', 'w') as f:
        for lines, value in all_files_sorted.items():
            for name, content in value.items():
                f.write(f'{name}\n')
                f.write(f'{str(lines)}\n')
                f.write(f'{content}\n')

files_sort(['1.txt', '2.txt', '3.txt'])