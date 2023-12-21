def sum_of_divisors_in_range(n):
    divisors = []
    for d in range(1, 1 + int(n ** .5) + 1):
        if n % d == 0:
            divisors.append(d)
            divisors.append(n // d)
    return sum(divisors[27:44] or [0])
