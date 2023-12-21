
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(5, 9):
        if n % i == 0 and i >= 5 and i <= 8:
            result += i
    return result
