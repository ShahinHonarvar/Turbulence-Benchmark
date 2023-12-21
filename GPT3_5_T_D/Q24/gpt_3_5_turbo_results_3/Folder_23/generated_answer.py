
def sum_of_divisors_in_range(number):
    divisors = [i for i in range(1, number+1) if number % i == 0]
    divisors_in_range = [x for x in divisors if 18 <= x <= 52]
    return sum(divisors_in_range) if divisors_in_range else 0
