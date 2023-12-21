def find_divisors_in_range(n):
    divisors = []
    for x in range(1, int(n ** .5) + 1):
        if n % x == 0:
            divisors.append(x)
            divisors.append(n // x)
    return [x for x in divisors if x in range(42, 77)]
