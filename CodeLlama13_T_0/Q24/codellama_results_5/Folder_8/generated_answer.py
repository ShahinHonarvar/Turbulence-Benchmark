
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(48, 63):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) or 0
