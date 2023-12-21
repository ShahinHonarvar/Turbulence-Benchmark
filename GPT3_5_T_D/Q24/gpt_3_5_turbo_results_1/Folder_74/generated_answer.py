
def sum_of_divisors_in_range(num):
    divisors = [x for x in range(1, num+1) if num % x == 0]
    divisors = [x for x in divisors if x >= 40 and x <= 74]
    return sum(divisors) if divisors else 0
