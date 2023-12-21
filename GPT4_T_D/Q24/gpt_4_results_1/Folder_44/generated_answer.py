
def sum_of_divisors_in_range(n):
    div_sum = 0
    for i in range(50, 85):
        if n % i == 0:
            div_sum += i
    return div_sum
