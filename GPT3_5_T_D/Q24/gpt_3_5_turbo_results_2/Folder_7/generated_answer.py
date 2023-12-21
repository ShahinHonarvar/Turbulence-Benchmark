
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0 and 469 <= i <= 682]
    return sum(divisors)
