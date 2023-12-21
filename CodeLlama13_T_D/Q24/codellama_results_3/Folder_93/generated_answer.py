
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(48, 93):
        if n % i == 0 and i >= 48 and i <= 92:
            result += i
    return result
