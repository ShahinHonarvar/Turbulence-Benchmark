
import math

def all_left_right_truncatable_prime(lim_tup):
    return sorted(set(left_right_truncatable_prime(lim_tup)), reverse=True)

def left_right_truncatable_prime(lim_tup):
    for num in range(2, int(math.sqrt(max(lim_tup)) + 1)):
        if is_left_right_truncatable_prime(num):
            yield num

def is_left_right_truncatable_prime(num):
    return num not in set(str(num)) and all(int(d) for d in str(num))
