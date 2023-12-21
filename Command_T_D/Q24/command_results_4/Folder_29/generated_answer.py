def sum_of_divisors_in_range(n):
    if n < 43 or n > 77:
        return 0
    divisors = set()
    for i in range(1, 1 + int(n**(0.5))):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)
