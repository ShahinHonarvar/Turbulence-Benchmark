
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x + 1):
        if all(str(i).count(c) == 1 for c in str(i)):
            res += [i]
    return res
