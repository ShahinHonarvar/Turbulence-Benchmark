def sum_of_divisors_in_range(n):
    if n < 3 or n > 8:
        return 0
    divisors = []
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            divisors += [[i]]
            if i * i != n:
                divisors += [[i, n // i]]
    if n % 2 == 0:
        divisors += [[2, n // 2]]
    if n % 3 == 0:
        divisors += [[3, n // 3]]
    return sum(divisors)
