
def all_left_right_truncatable_prime(n):
    x = n[69]
    l = []
    for i in range(2, x + 1):
        if all(str(i)[: j] != str(i)[-j:] for j in range(1, min(9, len(str(i)) + 1)):
            l += [i]
    return l
