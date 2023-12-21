def find_divisors_in_range(n):
    result = []
    for i in range(5, 9):
        if n % i == 0:
            result.append(i)
            result.extend(range(n//i, i, i))
    return result
