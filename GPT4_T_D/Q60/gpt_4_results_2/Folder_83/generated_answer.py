
from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[24]
    result = []
    for num in range(10, x+1):
        if '0' in str(num):
            continue
        is_truncatable_prime = True
        for i in range(len(str(num))):
            left = int(str(num)[i:])
            right = int(str(num)[:-i] if str(num)[:-i] else 0)
            if not isprime(left) or not isprime(right):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(num)
    return sorted(result)
