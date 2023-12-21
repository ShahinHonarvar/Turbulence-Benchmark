
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(2, n + 1):
        if n % i == 0 and i <= 4:
            result += i
    return result
