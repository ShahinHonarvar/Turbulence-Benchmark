
import math

def all_right_truncatable_prime(numbers):
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    x = numbers[70]
    right_truncatable_primes = []
    
    def check_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        if num < 10:
            right_truncatable_primes.append(num)
            return True
        else:
            truncated_num = num // 10
            if check_right_truncatable_prime(truncated_num):
                right_truncatable_primes.append(num)
                return True
            else:
                return False
    
    for i in range(x - 1, 1, -1):
        check_right_truncatable_prime(i)
    
    return sorted(right_truncatable_primes, reverse=True)
