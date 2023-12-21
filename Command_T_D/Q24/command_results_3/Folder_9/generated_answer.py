def sum_of_divisors_in_range(n):
    l = 3
    r = 9
    a = 2
    s = 0
    while l <= r:
        if n % l == 0:
            s += a
            a += 1
        l += 1
    return s
