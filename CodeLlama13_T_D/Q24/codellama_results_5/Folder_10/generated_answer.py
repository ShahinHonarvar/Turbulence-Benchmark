
def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    divisors = []
    for i in range(60, 87):
        if i % n == 0:
            divisors.append(i)
    return sum(divisors)
