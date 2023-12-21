import math
def sum_of_divisors_in_range(n):
    if n < 378 or n > 782:
        return 0
    upper_range_sum = math.factorial(int(math.sqrt(n))) / math.factorial(int(math.sqrt(n)) + 1)
    lower_range_sum = math.factorial(int(math.sqrt(n))) / math.factorial(int(math.sqrt(n)) - 1)
    return upper_range_sum - lower_range_sum
