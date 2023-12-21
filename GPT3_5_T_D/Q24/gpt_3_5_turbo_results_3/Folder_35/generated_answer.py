
def sum_of_divisors_in_range(num):
    divisors = [x for x in range(1, num+1) if num % x == 0]
    divisors_in_range = [x for x in divisors if 392 <= x <= 465]
    return sum(divisors_in_range) if divisors_in_range else 0
