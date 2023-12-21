import math
def find_divisors_in_range(n):
    lst = []
    for i in range(81, n // 2):
        if n % i == 0:
            lst.append(i)
            if i * i != n:
                lst.append(n // i)
    if n % 2 == 0:
        lst.append(2)
    return lst
