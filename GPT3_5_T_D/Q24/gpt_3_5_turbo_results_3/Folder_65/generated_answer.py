
def sum_of_divisors_in_range(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0 and 46 <= i <= 65:
            total += i
    return total
