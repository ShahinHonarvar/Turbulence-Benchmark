
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    right_truncatable_primes = []
    
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = str(num)
            is_right_truncatable_prime = True
            
            while temp != '':
                if not is_prime(int(temp)):
                    is_right_truncatable_prime = False
                    break
                temp = temp[:-1]
            
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
