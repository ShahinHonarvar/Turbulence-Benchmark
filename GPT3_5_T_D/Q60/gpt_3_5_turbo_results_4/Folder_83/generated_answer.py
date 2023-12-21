
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    x = numbers[24]
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        
        if is_prime(num):
            left_truncatable_prime = True
            right_truncatable_prime = True
            temp = str(num)
            
            while left_truncatable_prime and len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    left_truncatable_prime = False
            
            temp = str(num)
            while right_truncatable_prime and len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    right_truncatable_prime = False
            
            if left_truncatable_prime and right_truncatable_prime:
                truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
