
def sum_of_divisors_in_range(num):
    return sum(x for x in range(1, 8) if num % x == 0)
