def find_divisors_in_range(n):
    return [i for i in range(1, n + 1) if i * i <= n and n % i == 0]
