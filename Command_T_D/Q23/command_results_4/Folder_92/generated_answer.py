def find_divisors_in_range(x):
    result = []
    for divisor in range(8, x//2):
        if x % divisor == 0:
            result.append(divisor)
    return result
