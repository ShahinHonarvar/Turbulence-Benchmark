
def sum_of_divisors_in_range(n):
    if n < 36 or n > 93:
        return 0
    total = 0
    for i in range(36, 94):
        if n % i == 0:
            total += i
    return total
