
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 658 <= i <= 868]
    return sum(divisors) if divisors else 0
