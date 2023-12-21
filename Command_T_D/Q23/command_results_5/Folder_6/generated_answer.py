def find_divisors_in_range(n):
    if n <= 58:
        return []
    elif n >= 90:
        return []
    else:
        return [i for i in range(58, n // 2 + 1) if n % i == 0]
