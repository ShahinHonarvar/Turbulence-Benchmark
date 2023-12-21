def find_divisors_in_range(n):
    if n < 32 or n > 35:
        return []
    return [i for i in range(1, n) if n % i == 0]
