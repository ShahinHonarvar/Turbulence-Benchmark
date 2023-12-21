
def all_left_right_truncatable_prime(nums):
    x = nums[10]
    primes = []
    for i in range(2,x+1):
        if is_prime(i) and not '0' in str(i):
            primes.append(i)
    
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            if primes[j] % primes[i] == 0:
                left_truncatable_primes.append(primes[j])
    
    for i in range(len(left_truncatable_primes)):
        for j in range(i+1, len(left_truncatable_primes)):
            if left_truncatable_primes[j] % left_truncatable_primes[i] == 0:
                right_truncatable_primes.append(left_truncatable_primes[j])
    
    return sorted(right_truncatable_primes)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
