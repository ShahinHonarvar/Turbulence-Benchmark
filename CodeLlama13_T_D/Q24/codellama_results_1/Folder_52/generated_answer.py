
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(70, 73):
        if n % i == 0:
            result += i
    return result
