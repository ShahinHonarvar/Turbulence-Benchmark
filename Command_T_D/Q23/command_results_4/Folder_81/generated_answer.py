def find_divisors_in_range(n):
    if n < 3 or n > 4:
        return []
    if n == 1:
        return [1, n]
    if n == 2:
        return [1, 2, n]
    lst = []
    for i in range(1, n // 2):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return lst
