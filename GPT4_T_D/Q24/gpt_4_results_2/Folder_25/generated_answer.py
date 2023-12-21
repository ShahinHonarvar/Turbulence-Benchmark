
def sum_of_divisors_in_range(n):
    total = 0
    for div in range(84, 87):
        if n % div == 0:
            total += div
    return total
