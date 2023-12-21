
def sum_of_divisors_in_range(num):
    div_sum = 0
    for i in range(20, 51):
        if num % i == 0:
            div_sum += i
    return div_sum
