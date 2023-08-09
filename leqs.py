files = ['ok_1.txt', 'ok_2.txt']

for file in files:
    with open(file) as f:
        l = list(map(lambda x: x.replace('\n', ''), f.readlines()))
        print(len(l), len(set(l)))
