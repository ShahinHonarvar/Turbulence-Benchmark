
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[78]
    
    def check_lr_truncatable(num):
        num_str = str(num)
        return all(
            isprime(int(num_str[i:j])) 
            for i, j in product(range(len(num_str)), repeat=2) 
            if i < j and '0' not in num_str[i:j])
    
    return sorted(
