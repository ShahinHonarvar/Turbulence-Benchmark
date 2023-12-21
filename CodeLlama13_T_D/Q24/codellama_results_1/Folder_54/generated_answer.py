
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(36, 94):
        if n % i == 0 and i in range(36, 94):
            result += i
    return result
