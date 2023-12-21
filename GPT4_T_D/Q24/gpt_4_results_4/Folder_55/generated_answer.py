
def sum_of_divisors_in_range(n):
    divisor_list = [i for i in range(5, 9) if n % i == 0]
    return sum(divisor_list)
