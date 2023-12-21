def find_divisors_in_range(n):
    return [i for i in range(46, n // 2 + 1, n // 2) if n % i == 0]
