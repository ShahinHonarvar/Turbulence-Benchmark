
from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[22]
    truncatable_primes = []
    
    for num in range(10, x+1):
        if '0' not in str(num) and isprime(num):
            temp_str_num = str(num)
            flag = 0
            for i in range(len(temp_str_num)):
                if not isprime(int(temp_str_num[:len(temp_str_num) - i])):
                    flag = 1
                    break
                if not isprime(int(temp_str_num[i:])):
                    flag = 1
                    break
            
            if flag == 0:
                truncatable_primes.append(num)

    truncatable_primes.sort(reverse=True)
    return truncatable_primes
