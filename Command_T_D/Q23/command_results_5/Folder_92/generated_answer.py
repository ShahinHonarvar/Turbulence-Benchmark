def find_divisors_in_range(n):
    lst = []
    for i in range(8, n//2):
        if n % i == 0:
            lst.append(i)
    if n % 2 == 0:
        lst.append(2)
    return lst
