
def find_divisors_in_range(n):
    if n >= 3 and n <= 4:
        if n % 3 == 0 or n % 4 == 0:
            return [i for i in range(3, 5) if n % i == 0]
    return []
