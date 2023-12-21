
def sum_of_divisors_in_range(n):
    sum_value = 0
    for i in range(58, 91):
        if n % i == 0:
            sum_value += i
    return sum_value
