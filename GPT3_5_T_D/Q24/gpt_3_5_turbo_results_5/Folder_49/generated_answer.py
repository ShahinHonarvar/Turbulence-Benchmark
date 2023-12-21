
def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(2, 7):
        if num % i == 0:
            divisors.append(i)
    if divisors:
        return sum(divisors)
    else:
        return 0
