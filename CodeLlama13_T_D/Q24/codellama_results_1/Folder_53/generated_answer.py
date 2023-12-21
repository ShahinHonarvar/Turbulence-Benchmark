
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(4, 10):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) or 0
