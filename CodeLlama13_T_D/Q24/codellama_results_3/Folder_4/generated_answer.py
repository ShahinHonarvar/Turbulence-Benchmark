
def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(48, 61):
        if n % i == 0 and i <= 60:
            sum += i
    return sum
