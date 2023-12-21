def find_divisors_in_range(n):
    if n < 4:
        return []
    elif n < 6:
        return [i for i in range(3, n + 1) if n % i == 0]
    else:
        return [i for i in range(3, n // 2 + 1) if n % i == 0]
