import sys
def find_divisors_in_range(n):
    lst = []
    for i in range(315, 955+1):
        if n % i == 0:
            lst.append(i)
    return lst
