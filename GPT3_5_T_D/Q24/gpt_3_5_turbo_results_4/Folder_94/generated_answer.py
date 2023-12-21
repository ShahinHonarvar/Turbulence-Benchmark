
def sum_of_divisors_in_range(integer):
    divisors = [x for x in range(1, integer + 1) if integer % x == 0]
    return sum([x for x in divisors if 35 <= x <= 37]) if any(35 <= x <= 37 for x in divisors) else 0
