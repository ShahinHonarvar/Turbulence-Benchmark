
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(6, 9):
        if n % i == 0 and n / i >= 6:
            result += i
    return result
