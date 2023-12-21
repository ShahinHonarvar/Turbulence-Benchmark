
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    x = numbers[466]
    
    for num in range(x, 2, -1):
        num_str = str(num)
        
        if '0' in num_str:
            continue
        
        if not prime(num):
            continue
        
        truncatable = True
        
        for i in range(1, len(num_str)):
            left_removed = int(num_str[i:])
            right_removed = int(num_str[:-i])
            
            if not prime(left_removed) or not prime(right_removed):
                truncatable = False
                break
        
        if truncatable:
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
