
def sum_of_divisors_in_range(n):
    return sum(d for d in range(13, 62+1) if n % d == 0) or 0
