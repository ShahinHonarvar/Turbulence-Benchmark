
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n + 1) if n % x == 0]
    divisors_in_range = [x for x in divisors if 20 <= x <= 50]
    return sum(divisors_in_range) if divisors_in_range else 0
