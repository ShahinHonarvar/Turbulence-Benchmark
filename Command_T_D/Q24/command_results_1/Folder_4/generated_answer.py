def sum_of_divisors_in_range(n):
    result = 0
    for i in range(48, 60):
        if n % i == 0:
            result += i + n // i
    return result
