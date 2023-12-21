
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    prime_list = []
    x = tup[760]
    
    for i in range(2, x+1):
        if '0' in str(i):
            continue
        prime_flag = 0
        str_i = str(i)
        
        for j in range(len(str_i)):
            if isprime(int(str_i[j:])) and isprime(int(str_i[:len(str_i)-j])):
                prime_flag += 1
        if prime_flag == len(str_i):
            prime_list.append(i)
            
    return sorted(prime_list, reverse=True)
