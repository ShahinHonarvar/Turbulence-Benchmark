
from sympy import isprime

def all_left_truncatable_prime(nums_tuple):
    max_num = nums_tuple[96]
    result = []
    for num in range(10, max_num):
        if '0' in str(num):
            continue
        
        prime_flag = all(isprime(int(str(num)[i:])) for i in range(len(str(num))))
        if prime_flag:
            result.append(num)
            
    return sorted(result, reverse=True)
