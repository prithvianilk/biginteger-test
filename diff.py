delta = 0
with open(input()) as f1:
    with open(input()) as f2:
        l1, l2 = f1.readlines(), f2.readlines()
        for (x, y) in zip(l1, l2):
            delta += int(x != y)
        uniq = set(l1 + l2)
        print('are all values in each list unique?', len(uniq) == len(l1) + len(l2))
        print('how many differences are there line by line?', delta)

