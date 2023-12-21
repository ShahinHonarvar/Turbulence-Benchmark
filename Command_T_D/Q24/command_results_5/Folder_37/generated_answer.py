def sum_of_divisors_in_range(n):
    if n < 3 or n > 7:
        return 0
    d = set(str(n))
    for i in range(3, n):
        if set(str(i)) <= d:
            return sum(divmod(i, x) for x in range(1, i))
    return 0
