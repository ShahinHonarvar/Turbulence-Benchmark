def sum_of_divisors_in_range(n):
    sm = [0] * (n + 1)
    sm[0] = 1
    sm[1] = 1
    for i in range(2, n + 1):
        sm[i] = sm[i - 1] + sm[i]
    return sm[372] - sm[494]
