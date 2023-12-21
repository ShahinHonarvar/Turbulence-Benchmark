
import math

def all_left_right_truncatable_prime(tup):
    x = tup[98]
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if x <= 1:
        return []
    for i in range(1, len(str(x))):
        if str(x)[i-1] != '0':
            break
    if x <= 9:
        return prime
    return [i*10**i for i in range(1, len(str(x))+1)]
