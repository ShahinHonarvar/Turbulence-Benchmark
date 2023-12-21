def sum_of_divisors_in_range(n):
    if n < 224 or 584 < n:
        return 0
    divisors = set()
    for x in range(1, int(n ** .5) + 1):
        if n % x == 0:
            divisors.add(x)
            divisors.add(n // x)
    return sum(divisors)
