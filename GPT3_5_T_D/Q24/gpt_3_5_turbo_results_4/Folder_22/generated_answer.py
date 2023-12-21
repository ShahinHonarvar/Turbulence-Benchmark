
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n+1) if n % x == 0]
    return sum([x for x in divisors if 4 <= x <= 7]) if any(4 <= x <= 7 for x in divisors) else 0
