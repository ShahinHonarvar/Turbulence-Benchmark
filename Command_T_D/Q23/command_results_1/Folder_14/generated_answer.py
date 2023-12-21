def find_divisors_in_range(n):
    if n < 6 or n > 8:
        return []
    lst = []
    for i in range(6, 8):
        if n % i == 0:
            lst.append(i)
    if n == 6 or n == 8:
        lst.append(n)
    return lst
