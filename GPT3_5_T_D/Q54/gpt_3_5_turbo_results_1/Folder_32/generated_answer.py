 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    truncatable_primes = []
    
    for i in range(2, x):
        num = str(i)
        is_right_truncatable = True
        
        while num:
            if not is_prime(int(num)):
                is_right_truncatable = False
                break
            num = num[:-1]
        
        if is_right_truncatable:
            truncatable_primes.append(i)
    
    return sorted(truncatable_primes)
