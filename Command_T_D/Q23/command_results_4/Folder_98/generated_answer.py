import sys
def find_divisors_in_range(n):
    x = []
    for i in range(3, 9):
        if n % i == 0:
            x.append(i)
            if i != n // i:
                x.append(n // i)
    return x
