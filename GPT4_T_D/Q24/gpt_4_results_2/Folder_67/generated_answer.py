
def sum_of_divisors_in_range(number):
    sum_divisors = 0
    for i in range(33, 58):
        if number % i == 0:
            sum_divisors += i
    return sum_divisors
