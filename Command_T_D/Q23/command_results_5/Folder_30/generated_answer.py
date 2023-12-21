def find_divisors_in_range(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    lst = sorted(set(lst))
    if lst[0] <= 42 and lst[-1] >= 77:
        return lst
    else:
        return []
