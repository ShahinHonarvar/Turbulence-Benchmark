
def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(36, 94):
        if n % i == 0 and i <= 93:
            sum += i
    return sum
