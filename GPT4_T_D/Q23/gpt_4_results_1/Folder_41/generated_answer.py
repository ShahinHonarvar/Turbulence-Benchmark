
def find_divisors_in_range(n):
    if n <= 1:
        return []
    else:
        return [i for i in range(2, 5) if n % i == 0]
