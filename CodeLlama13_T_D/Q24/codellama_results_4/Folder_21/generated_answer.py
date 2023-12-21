
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(120, 350):
        if n % i == 0 and i > 1:
            result += i
    return result
