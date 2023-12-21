
def sum_of_divisors_in_range(n):
    if n < 33 or n > 57:
        return 0
    return sum(i for i in range(33, 58) if n % i == 0)
