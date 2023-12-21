
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    
    for num in range(2, x):
        string_num = str(num)
        prime = True
        while len(string_num) > 0:
            if not isprime(int(string_num)):
                prime = False
                break
            else:
                string_num = string_num[:-1]
                
        if prime:
            result.append(num)
            
    result.sort(reverse=True)
    return result
