def find_divisors_in_range(x):
    return [i for i in range(x, x+1, x) if x % i == 0]
