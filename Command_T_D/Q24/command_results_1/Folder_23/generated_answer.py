def sum_of_divisors_in_range(n):
    if n <= 17 or n >= 53:
        return 0
    result = 0
    for i in range(18, 52):
        if n % i == 0:
            result += i
    if n > 1:
        result += n
    return result
