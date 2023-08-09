delta = 0
with open('ok_1.txt') as f1:
    with open('ok_2.txt') as f2:
        l1, l2 = f1.readlines(), f2.readlines()
        for (x, y) in zip(l1, l2):
            delta += int(x != y)
        total = set(l1 + l2)
        print(len(total) == len(l1) + len(l2))
        print(delta)

