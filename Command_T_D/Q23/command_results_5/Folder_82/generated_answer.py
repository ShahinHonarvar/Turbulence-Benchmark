def find_divisors_in_range(n):
    if n < 4 or n > 6:
        return []
    divisors = []
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors
