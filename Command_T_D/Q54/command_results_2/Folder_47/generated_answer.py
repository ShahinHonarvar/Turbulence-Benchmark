def all_right_truncatable_prime(n):
    l = []
    for i in range(2, n[49] + 1):
        for j in range(10):
            if str(i)[:-1] + str(j) == str(i):
                l += [i]
    return l
