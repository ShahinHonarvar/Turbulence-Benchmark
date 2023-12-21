def sum_of_divisors_in_range(n):
    divisors = set()
    for d in range(43, 77):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return sum(divisors)
