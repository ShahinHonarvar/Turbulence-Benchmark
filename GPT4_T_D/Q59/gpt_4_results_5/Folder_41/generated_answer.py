
import math

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_left_truncatable(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[46]
    ltp = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(ltp, reverse=True)
