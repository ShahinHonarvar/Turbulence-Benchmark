def find_divisors_in_range(n):
    if n < 6 or n > 9:
        return []
    lst = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            lst.append(i)
            if i * i != n:
                lst.append(n // i)
    return lst
