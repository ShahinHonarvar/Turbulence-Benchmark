def find_divisors_in_range(n):
    lst = []
    for x in range(43, 47):
        if n % x == 0:
            lst.append(x)
            lst.append(n//x)
    return lst
