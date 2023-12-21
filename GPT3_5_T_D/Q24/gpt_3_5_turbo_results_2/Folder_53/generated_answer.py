
def sum_of_divisors_in_range(integer):
    divisors = []
    for i in range(4, 10):
        if integer % i == 0:
            divisors.append(i)
    return sum(divisors) if divisors else 0
