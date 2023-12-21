def sum_of_divisors_in_range(x):
    return sum(div for div in range(744, 885) if x % div == 0)
