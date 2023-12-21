
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n+1) if n % x == 0]
    sum_of_divisors = sum([x for x in divisors if 372 <= x <= 494])
    return sum_of_divisors if sum_of_divisors != 0 else 0
