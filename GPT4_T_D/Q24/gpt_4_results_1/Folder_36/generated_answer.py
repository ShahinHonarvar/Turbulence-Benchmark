
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(113, 992) if n % i == 0]
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)
