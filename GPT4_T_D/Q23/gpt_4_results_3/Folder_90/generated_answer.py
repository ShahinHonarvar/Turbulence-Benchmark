
def find_divisors_in_range(n):
    divisors = [i for i in range(451, 974) if n % i == 0]
    return divisors
