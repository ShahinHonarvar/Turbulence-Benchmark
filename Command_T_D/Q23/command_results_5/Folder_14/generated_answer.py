def find_divisors_in_range(x):
    return [i for i in range(x, min(x+5, x+10), 2) if x % i == 0]
