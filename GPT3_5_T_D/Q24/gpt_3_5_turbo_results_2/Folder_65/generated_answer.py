
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 46 <= i <= 65]
    return sum(divisors) if divisors else 0
