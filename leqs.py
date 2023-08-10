files = [input(), input()]

for file in files:
    with open(file) as f:
        l = list(map(lambda x: x.replace('\n', ''), f.readlines()))
        print(f'for {file}, are there any duplicates?', len(l) != len(set(l)))
