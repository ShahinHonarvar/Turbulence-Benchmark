
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(744, 885+1):
        if i % n == 0:
            result += i
    return result
