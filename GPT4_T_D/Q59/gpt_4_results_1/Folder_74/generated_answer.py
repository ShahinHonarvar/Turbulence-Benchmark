
import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        max_div = math.floor(math.sqrt(n))
        for i in range(3, 1 + max_div, 2):
            if n % i == 0:
                return False
        return True
      
def is_left_truncatable(n):
    str_num = str(n)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):  
    x = tup[36]
    result = []
    for num in range(1,x):
        if is_prime(num) and is_left_truncatable(num):
            result.append(num)
    return sorted(result)
