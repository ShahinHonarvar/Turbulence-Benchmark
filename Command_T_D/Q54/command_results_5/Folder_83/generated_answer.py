import sys
def all_right_truncatable_prime(tup):
    x = tup[24]
    y = x - 1
    if x > 2:
        return []
    for i in range(2, x):
        if x % i == 0:
            continue
        if all(x % d == 0 for d in range(x, x//i, i)):
            break
        if all(x % d == 0 for d in range(x, x//i, i)):
            break
        else:
            return [i]
    if x == 2:
        return [2]
    for i in range(3, x):
        if x % i == 0:
            continue
        if all(x % d == 0 for d in range(x, x//i, i)):
            break
        if all(x % d == 0 for d in range(x, x//i, i)):
            break
        else:
            return [i]
    return []
