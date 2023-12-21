def find_divisors_in_range(n):
    if n <= 6:
        return []
    elif n == 7:
        return [i for i in range(1, n // 2) if n % i == 0]
    elif n == 8:
        return [i for i in range(1, n // 2) if n % i == 0]
