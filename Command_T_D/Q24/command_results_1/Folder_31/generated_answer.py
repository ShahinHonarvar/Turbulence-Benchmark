def sum_of_divisors_in_range(n):
    if n < 35 or n > 55:
        return 0
    divisor_set = set()
    for i in range(1, 1 + int(n ** .5)):
        if n % i == 0:
            divisor_set.add(i)
            if i * i != n:
                divisor_set.add(n // i)
    return sum(divisor_set)
