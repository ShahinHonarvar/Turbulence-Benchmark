
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(3, 6) if n % x == 0]
    if divisors:
        return sum(divisors)
    else:
        return 0
