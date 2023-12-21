
import sys

def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(3, int(str(x)[-1])+1):
        if all(i%n == 0 for n in range(2, int(str(i)[-1])+1)):
            lst.append(i)
    return sorted(set(lst))
