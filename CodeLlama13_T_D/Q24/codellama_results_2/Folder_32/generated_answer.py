
def sum_of_divisors_in_range(n):
    result = 0
    for i in range(71, 82):
        if n % i == 0 and i <= 81:
            result += i
    return result
