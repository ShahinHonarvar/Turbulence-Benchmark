def sum_of_divisors_in_range(n):
    if n < 35 or n > 98:
        return 0
    s = set()
    for d in range(35, 98):
        if n % d == 0:
            s.add(d)
            if d * d != n:
                s.add(n // d)
    return sum(s)
