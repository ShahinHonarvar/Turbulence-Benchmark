
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x // 2 + 1):
        if i % 2 == 1:
            if all(str(i).count(d) == 1 for d in str(i)):
                res += [i]
    for i in range(3, x // 2 + 1, 2):
        if i % 2 == 1:
            if all(str(i).count(d) == 1 for d in str(i)):
                res += [i]
    for i in range(5, x // 2 + 1, 5):
        if i % 2 == 1:
            if all(str(i).count(d) == 1 for d in str(i)):
                res += [i]
    return sorted(res)
