
def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for i in range(50, 82):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors
