def find_divisors_in_range(n):
    result = []
    for i in range(392, 465):
        if n % i == 0:
            result.append(i)
            result += range(1, int(n / i) + 1)
    return result
