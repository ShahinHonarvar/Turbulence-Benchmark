
def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(378, 782+1):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) if divisors else 0
