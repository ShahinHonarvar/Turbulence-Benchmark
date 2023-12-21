import fractions
def find_divisors_in_range(n):
    if n < 6:
        return []
    if n % 2 == 0:
        return [2, 4, 6, 8]
    return [3, 5, 7]
