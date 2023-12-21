
def sum_of_divisors_in_range(n):
    if n < 1:
        return "Enter a Positive Integer"
    divisors = [i for i in range(744, 886) if n % i == 0]
    return sum(divisors) if divisors else 0
