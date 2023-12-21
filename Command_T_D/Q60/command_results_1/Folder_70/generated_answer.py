
import math

def all_left_right_truncatable_prime(x_range):
    # y = min(x_range)
    # x = max(x_range)
    y = x_range[0]
    x = x_range[1]
    return sorted((n for n in range(y, x+1) if is_left_right_truncatable_prime(n)), reverse=True)

def is_left_right_truncatable_prime(n):
    # x = math.sqrt(n)
    # for i in range(1, int(math.sqrt(n))+1):
    #     if n % i == 0:
    #         return False
    # return True
    return n % 2 == 1 and all(n % i != 0 for i in range(3, int(math.sqrt(n))+1))
