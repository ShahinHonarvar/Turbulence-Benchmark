
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(7, num+1) if num % i == 0]
    return sum(divisors) if divisors else 0
