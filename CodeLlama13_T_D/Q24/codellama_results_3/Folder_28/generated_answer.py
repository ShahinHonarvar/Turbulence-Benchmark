
def sum_of_divisors_in_range(n):
    total = 0
    for i in range(16, 54):
        if n % i == 0 and i <= n:
            total += i
    return total
