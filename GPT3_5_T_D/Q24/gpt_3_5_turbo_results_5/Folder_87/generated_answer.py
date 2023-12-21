
def sum_of_divisors_in_range(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0 and 50 <= i <= 81:
            total += i
    return total
