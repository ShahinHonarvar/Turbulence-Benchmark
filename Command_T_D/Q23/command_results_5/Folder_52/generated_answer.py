def find_divisors_in_range(n):
    result = []
    for i in range(70, 73):
        if n % i == 0:
            result.append(i)
            if n != i**2:
                result.append(n//i)
    return result
