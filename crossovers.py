import random
from gene import Gene


def aox(l1, l2):
    n = len(l1)
    child = [Gene()] * n
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    if x == y:
        y = x+1
    i, j = sorted([x, y])

    child[i:j] = l1[i:j]

    for r in range(0, n):
        if child[r].name is None:
            if l2[r] not in child[0:n]:
                child[r] = l2[r]
            else:
                for t in range(0, n):
                    if l2[t] not in child[0:n]:
                        child[r] = l2[t]
                        break
    return child


def aox_2(l1, l2):
    child1 = aox(l1, l2)
    child2 = aox(l2, l1)
    return child1, child2


def ox(l1, l2):
    n = len(l1)
    child = [None] * n
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    if x == y:
        y = x + 1
    i, j = sorted([x, y])
    child = list(l2)
    for r in range(0,n):
        if child[r] in l1[i:j]:
            child[r] = None
    child = child[i:n] + child[0:i]
    indexes = [aux for aux in range(n) if child[aux] is None]
    for k in range(len(indexes)):
        child.remove(None)
    child = child[0:i] + l1[i:j] + child[i:n]
    return child


def ox_2(l1,l2):
    return ox(l1, l2), ox(l2, l1)
