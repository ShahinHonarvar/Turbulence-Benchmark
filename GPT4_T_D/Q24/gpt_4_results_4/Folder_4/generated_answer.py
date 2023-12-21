
def sum_of_divisors_in_range(n):
    divisors_in_range = [i for i in range(48, 61) if n % i ==0]
    return sum(divisors_in_range)
