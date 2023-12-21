
def sum_of_divisors_in_range(n):
    total = 0
    for i in range(2, n+1):
        if i % n == 0 and 20 <= i <= 50:
            total += i
    return total
