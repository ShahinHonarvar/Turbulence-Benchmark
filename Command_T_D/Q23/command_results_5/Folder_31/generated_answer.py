import sys
def find_divisors_in_range(n):
    res = []
    for i in range(35, 55):
        if n % i == 0:
            res.append(i)
            if n // i == i:
                break
    return res
