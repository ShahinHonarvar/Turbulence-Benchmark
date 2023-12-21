
def sum_of_divisors_in_range(n):
    sum_range = 0
    for i in range(84, 87):
        if n % i == 0:
            sum_range += i
    return sum_range
