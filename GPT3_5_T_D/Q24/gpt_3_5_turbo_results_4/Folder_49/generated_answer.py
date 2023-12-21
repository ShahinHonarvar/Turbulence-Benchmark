
def sum_of_divisors_in_range(integer):
    divisors = [i for i in range(2, 7) if integer % i == 0]
    if divisors:
        return sum(divisors)
    else:
        return 0
