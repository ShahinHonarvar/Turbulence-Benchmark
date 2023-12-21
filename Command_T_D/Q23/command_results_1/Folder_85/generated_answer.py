def find_divisors_in_range(n):
    result = []
    for i in range(2, n+1):
        for j in range(2, i+1):
            if i % j == 0:
                result.append(i)
                break
    return result
