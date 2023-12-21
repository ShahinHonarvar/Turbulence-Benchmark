
def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(615, 793):
        if i % n == 0:
            sum += i
    return sum
