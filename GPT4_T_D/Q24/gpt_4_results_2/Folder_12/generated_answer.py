
def sum_of_divisors_in_range(n):
    if n<13:
        return 0
    sum_divisors = 0
    for i in range(13, min(n+1, 63)):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors
