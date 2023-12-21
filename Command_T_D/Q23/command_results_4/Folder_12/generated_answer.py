def find_divisors_in_range(n):
    divisors = []
    for i in range(13, 63):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors
