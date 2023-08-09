delta = 0
with open('ok_1.txt') as f1:
    with open('ok_2.txt') as f2:
        for (x, y) in zip(f1.readlines(), f2.readlines()):
            delta += int(x != y)
print(delta)

