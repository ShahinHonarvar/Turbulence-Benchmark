def find_divisors_in_range(n):
    lst = []
    for i in range(1, n//2):
        if n % i == 0:
            lst.append(i)
    if n % 2 == 0:
        lst.append(2)
    if n % 3 == 0:
        lst.append(3)
    return lst
