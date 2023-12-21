
def sum_of_divisors_in_range(integer):
    divisors = [i for i in range(1, integer+1) if integer % i == 0 and 392 <= i <= 465]
    return sum(divisors) if divisors else 0
