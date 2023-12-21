
def all_left_right_truncatable_prime(x_range):
    res = []
    for x in range(3, x_range[0] // 2):
        if all(str(x).count(c) == 1 for c in str(x)):
            res += [x]
    for x in range(x_range[0] // 2, x_range[1] // 2):
        if all(str(x).count(c) == 1 for c in str(x)):
            res += [x]
    return sorted(set(res))
