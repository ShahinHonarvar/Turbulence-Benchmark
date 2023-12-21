
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n+1) if n % x == 0]
    return sum([divisor for divisor in divisors if 472 <= divisor <= 827])
