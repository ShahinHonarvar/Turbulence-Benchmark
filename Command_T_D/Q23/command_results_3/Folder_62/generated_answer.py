def find_divisors_in_range(n):
    return [i for i in range(1, n // 2) if n % i == 0 and 59 <= i <= 88]
