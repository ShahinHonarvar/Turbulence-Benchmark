def find_divisors_in_range(n):
    divisors = []
    for i in range(1, 10):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors
