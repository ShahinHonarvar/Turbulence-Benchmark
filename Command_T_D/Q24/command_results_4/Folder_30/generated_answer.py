def sum_of_divisors_in_range(n):
    return sum(
        d
        for d in range(1, int(n ** .5) + 1)
        if d * d <= n and n % d == 0
    )
