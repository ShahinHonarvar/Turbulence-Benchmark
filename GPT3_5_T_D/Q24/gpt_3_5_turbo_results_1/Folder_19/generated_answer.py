
def sum_of_divisors_in_range(num):
    return sum(i for i in range(1, 8) if num % i == 0)
