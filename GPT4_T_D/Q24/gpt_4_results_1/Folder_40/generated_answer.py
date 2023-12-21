
def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    sum_of_divisors=0
    for i in range(1,3):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors
