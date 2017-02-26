import random


def twors(l1):
    n = len(l1)
    child = list(l1)
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    i, j = sorted([x, y])
    child[i], child[j] = child[j], child[i]
    return child


def rsm(l1):
    n = len(l1)
    child = list(l1)
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    i, j = sorted([x, y])
    while True:
        child[i], child[j] = child[j], child[i]
        i += 1
        j -= 1
        if i >= j:
            break
    return child


def psm(l1,pp):
    n = len(l1)
    child = list(l1)
    for i in range(n):
        p = random.uniform(1, pp)
        if p >= pp:
            j = random.randint(0, n-1)
            child[i], child[j] = child[j], child[i]
    return child


t1 = ['Q', 'B', 'C', 'A', 'D', 'Z', 'X', 'P', 'T', 'W']

for i in range(100):
    print twors(t1)
    print rsm(t1)
    print psm(t1, 0.4)