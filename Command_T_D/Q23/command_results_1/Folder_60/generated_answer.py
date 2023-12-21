def find_divisors_in_range(n):
    l = list(range(41, n, 1))
    m = list(range(n + 1, 55, 1))
    return [x for x in l if n % x == 0] + [x for x in m if n % x == 0]
