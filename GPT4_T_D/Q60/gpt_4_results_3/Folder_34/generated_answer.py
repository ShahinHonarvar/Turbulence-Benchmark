
from itertools import product

def all_left_right_truncatable_prime(nums):
    x = nums[18]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_all_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:len(num_str)-i])):
                return False
        return True
        
    all_truncatable_primes = []
    for digits in product(range(1,10), repeat=len(str(x))):
        num = int(''.join(str(digit) for digit in digits))
        if num > x:
            break
        if num < 10:
            all_truncatable_primes.append(num) if is_prime(num) else None
        else:
            all_truncatable_primes.append(num) if is_all_truncatable_prime(num) else None
    return sorted(all_truncatable_primes, reverse=True)
