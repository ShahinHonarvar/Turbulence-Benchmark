
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[784]
    return sorted([n for n in range(1, x+1) if is_left_right_truncatable_prime(n)])
