def find_divisors_in_range(n):
    if n <= 10 or n >= 42:
        return []
    else:
        return [i for i in range(11, n // 2 + 1) if n % i == 0]
