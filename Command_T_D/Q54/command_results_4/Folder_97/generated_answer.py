def all_right_truncatable_prime(n):
    res = []
    for i in range(3, int(str(n)[-1]) + 1):
        for j in range(3, int(str(n)[-1]) + 1):
            if str(n)[-1] == str(i) + str(j):
                res += [i * 10**(j - 1)]
    return res
