
def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(378, 782+1):
        if i % n == 0:
            sum += i
    return sum
