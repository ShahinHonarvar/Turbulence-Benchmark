
import math

def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i, int(math.sqrt(n)) + 1):
            if all(str(i).count(d) == 1 for d in str(i)):
                if all(str(j).count(d) == 1 for d in str(j)):
                    if is_prime(i) and is_prime(j):
                        res += [i]
    return res

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n % 5 == 0 or n % 7 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
