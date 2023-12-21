
def sum_of_divisors_in_range(n):
    if n < 1 or n > 9:
        return 0
    return sum(i for i in range(1, 10) if n % i == 0)
