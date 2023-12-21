def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, 1 + int(n ** .5)):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sum(divisors) if divisors else 0
