
def find_divisors_in_range(n):
    assert n > 0, "Input must be a positive integer"
    return [i for i in range(6, 10) if n % i == 0]
