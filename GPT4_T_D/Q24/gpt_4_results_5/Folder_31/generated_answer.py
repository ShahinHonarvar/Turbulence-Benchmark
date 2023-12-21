
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(35, 56) if n % i == 0]
    if not divisors:
        return 0
    return sum(divisors)
