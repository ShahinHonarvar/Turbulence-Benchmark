import sys
def find_divisors_in_range(n):
    res = []
    for i in range(315, 955):
        if n%i == 0:
            res.append(i)
            res += [n//i]
    return res
