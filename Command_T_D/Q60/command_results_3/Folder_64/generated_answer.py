
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, int(str(x)[-1]) + 1):
        if all(str(i)[: j] == str(i)[-j:] == str(i) for j in range(1, len(str(i)) + 1)):
            res += [i]
    return res
