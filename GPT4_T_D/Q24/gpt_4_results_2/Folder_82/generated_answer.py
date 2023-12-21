
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(4, 7):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) if divisors else 0
