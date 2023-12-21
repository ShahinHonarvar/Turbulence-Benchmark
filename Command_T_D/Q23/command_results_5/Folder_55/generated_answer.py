def find_divisors_in_range(x):
    return [i for i in range(5, x // 2 + 1) if x % i == 0]
