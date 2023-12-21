
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n+1) if n % x == 0]
    divisors_in_range = [x for x in divisors if 14 <= x <= 93]
    return sum(divisors_in_range) if len(divisors_in_range) > 0 else 0
