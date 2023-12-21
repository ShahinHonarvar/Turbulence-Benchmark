def find_divisors_in_range(n):
    lst = []
    for i in range(38, 65):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return lst
