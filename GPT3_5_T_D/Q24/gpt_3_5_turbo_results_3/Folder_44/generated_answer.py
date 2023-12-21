
def sum_of_divisors_in_range(integer):
    sum_divisors = 0
    for i in range(50, 85):
        if integer % i == 0:
            sum_divisors += i
    return sum_divisors
