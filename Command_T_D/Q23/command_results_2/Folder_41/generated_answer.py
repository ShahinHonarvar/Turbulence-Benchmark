def find_divisors_in_range(n):
    d = [2, 3]
    while d[-1] <= n:
        d.append(d[-1] + d[-2])
    return d[2:-2]
