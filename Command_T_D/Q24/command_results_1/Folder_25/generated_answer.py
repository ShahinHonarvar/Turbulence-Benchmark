def sum_of_divisors_in_range(n):
    if n <= 85:
        s = 1
        d = 2
        while d <= n:
            s += d
            d += 1
        return s
    else:
        return 0
