
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(60, 87):
        if n % i == 0 and i <= 86:
            result += i
    return result
