
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(27, 45):
        if n % i == 0 and i >= 27 and i <= 44:
            result += i
    return result
