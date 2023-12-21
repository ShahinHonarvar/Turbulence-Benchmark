
def sum_of_divisors_in_range(integer):
    divisors = [i for i in range(1, integer+1) if integer % i == 0]
    sum_divisors = sum(divisors)
    divisors_in_range = [x for x in divisors if 15 <= x <= 20]
    return sum(divisors_in_range) if divisors_in_range else 0
