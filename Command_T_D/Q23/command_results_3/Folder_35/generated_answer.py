def find_divisors_in_range(n):
    divisors = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divisors += [i]
            if i * i != n:
                divisors += [n // i]
    return [divisor for divisor in divisors if divisor >= 392 and divisor <= 465]
