
def sum_of_divisors_in_range(n):
    if n < 39 or n > 43:
        return 0
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0 and i >= 39 and i <= 43:
            divisors.append(i)
            if n // i != i and n // i >= 39 and n // i <= 43:
                divisors.append(n // i)
    return sum(divisors)
