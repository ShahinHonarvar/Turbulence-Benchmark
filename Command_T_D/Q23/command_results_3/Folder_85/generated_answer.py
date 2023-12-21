def find_divisors_in_range(n):
    if n < 2 or n > 5:
        return []
    return [i for i in range(2, n // 2) if n % i == 0]
