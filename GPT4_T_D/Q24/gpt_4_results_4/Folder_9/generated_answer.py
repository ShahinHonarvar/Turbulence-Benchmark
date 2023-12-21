
def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(3, 10):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors
