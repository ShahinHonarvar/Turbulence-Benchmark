
def sum_of_divisors_in_range(n):
    summation = 0
    for i in range(3, n+1):
        if n % i == 0 and i >= 3 and i <= 8:
            summation += i
    return summation
