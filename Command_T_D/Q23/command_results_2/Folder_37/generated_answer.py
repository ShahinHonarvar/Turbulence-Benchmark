import math
def find_divisors_in_range(n):
    lst = []
    for i in range(3,n+1):
        if i%2 == 0 and i != 0 and i != 1:
            lst.append(i)
            lst += find_divisors_in_range(i)
    return lst
