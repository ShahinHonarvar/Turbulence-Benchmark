
def sum_of_divisors_in_range(num):
    return sum(i for i in range(10, 70) if num % i == 0)
