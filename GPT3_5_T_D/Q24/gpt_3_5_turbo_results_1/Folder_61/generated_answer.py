
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(2, n + 1) if n % x == 0]
    divisors_in_range = [x for x in divisors if 2 <= x <= 3]
    return sum(divisors_in_range)
