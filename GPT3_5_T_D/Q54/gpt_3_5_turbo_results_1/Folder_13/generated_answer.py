
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[784]
    result = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            temp = i
            while temp > 0:
                temp //= 10
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(i)
    return sorted(result)
