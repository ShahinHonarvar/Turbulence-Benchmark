
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n + 1) if n % x == 0 and 15 <= x <= 92]
    return sum(divisors) if divisors else 0
