
def sum_of_divisors_in_range(n):
    return sum(d for d in range(451, 973+1) if n % d == 0) or 0
