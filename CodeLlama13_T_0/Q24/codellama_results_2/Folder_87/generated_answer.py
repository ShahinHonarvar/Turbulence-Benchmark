
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(50, 81):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) or 0
