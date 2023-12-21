
def sum_of_divisors_in_range(number):
    total_sum = 0
    for i in range(16, 69):
        if number % i == 0:
            total_sum += i
    return total_sum
