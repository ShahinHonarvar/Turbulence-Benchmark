def find_divisors_in_range(n):
    lst = []
    for i in range(57, 86):
        if n % i == 0:
            lst.append(i)
    if lst == []:
        return []
    return lst
