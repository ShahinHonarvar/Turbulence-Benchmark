
def sum_of_divisors_in_range(n):
    if n < 2:
        return 0

    divisors = [i for i in range(2, 10) if n % i == 0]
    return sum(divisors)
