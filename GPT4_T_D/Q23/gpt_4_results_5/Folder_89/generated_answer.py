
def find_divisors_in_range(n):
    divisors = [i for i in range(14, 49) if n % i == 0]
    return divisors
