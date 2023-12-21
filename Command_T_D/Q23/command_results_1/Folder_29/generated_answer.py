def find_divisors_in_range(n):
    lst = []
    for i in range(43, 77 + 1):
        if n % i == 0:
            lst.append(i)
    if len(lst) == 0:
        return []
    else:
        return lst
