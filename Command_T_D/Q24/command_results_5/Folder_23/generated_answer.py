def sum_of_divisors_in_range(n):
    result = 0
    for i in range(18, n // 2):
        if n % i == 0:
            result += i
            if i * i != n:
                result += n // i
    return result
