def find_divisors_in_range(n):
    if n <= 60:
        return []
    elif n <= 65:
        return [i for i in range(1, n + 1) if i*i <= n]
    elif n <= 85:
        return [i for i in range(1, n + 1) if i*i <= n and n % i == 0]
    elif n <= 86:
        return [i for i in range(1, n + 1) if i*i <= n and n % i == 0 and i >= 60 and i <= 86]
