
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(120, 349+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)
