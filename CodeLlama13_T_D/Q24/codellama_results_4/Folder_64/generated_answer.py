
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, 10):
        if n % i == 0 and i <= 9:
            divisors.append(i)
    return sum(divisors) or 0
