def find_divisors_in_range(n):
    if n < 228 or n > 846:
        return []
    divisors = []
    for i in range(1, 1 + int(n ** .5)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors
