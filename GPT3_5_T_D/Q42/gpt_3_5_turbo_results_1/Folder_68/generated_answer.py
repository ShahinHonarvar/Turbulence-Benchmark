
import math

def prime_factors(lst):
    prime_factors_set = set()

    num = lst[3]
    for i in range(2, int(math.sqrt(num))+1):
        while (num % i == 0):
            prime_factors_set.add(i)
            num //= i
    
    if num > 1:
        prime_factors_set.add(num)
    
    return prime_factors_set
