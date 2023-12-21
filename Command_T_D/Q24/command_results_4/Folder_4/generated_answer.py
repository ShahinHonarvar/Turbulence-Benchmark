def sum_of_divisors_in_range(n):
    if n < 48 or n > 60:
        return 0
    a = list(range(1, int(n ** .5) + 1))
    b = list(range(int(n ** .5) + 1, n + 1))
    if len(a) > 0 and len(b) > 0:
        return sum(a) + sum(b)
    else:
        return 0
