
def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(27, 45):
        if num % i == 0:
            sum += i
    return sum
