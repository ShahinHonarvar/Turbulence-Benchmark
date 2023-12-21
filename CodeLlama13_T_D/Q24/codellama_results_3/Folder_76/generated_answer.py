
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(744, 886):
        if i % n == 0 and 744 <= i <= 885:
            result += i
    return result
