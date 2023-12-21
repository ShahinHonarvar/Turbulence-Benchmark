
def find_divisors_in_range(n):
    divisors = []
    for d in range(42, 78):
        if n % d == 0:
            divisors.append(d)
    return divisors
