
def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    else:
        divisors = [i for i in range(2, n + 1) if n % i == 0]
        sum_of_divisors = sum(divisors)
        return sum_of_divisors
