import math
def find_divisors_in_range(n):
    if n < 372 or n > 494:
        return []
    lst = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            lst.append(i)
            if i * i != n:
                lst.append(n // i)
    return lst
