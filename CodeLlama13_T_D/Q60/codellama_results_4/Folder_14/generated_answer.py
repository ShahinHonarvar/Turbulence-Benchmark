
def all_left_right_truncatable_prime(x):
    left_truncatable_primes = []
    right_truncatable_primes = []
    
    for i in range(1, x+1):
        if is_prime(i):
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
            
    for i in range(2, int(x/2)):
        if is_prime(left_truncatable_primes[i]):
            left_truncatable_primes = left_truncatable_primes[:i+1]
            
    for i in range(len(right_truncatable_primes)-1, 0, -1):
        if is_prime(right_truncatable_primes[i]):
            right_truncatable_primes = right_truncatable_primes[:i+1]
            
    return sorted(left_truncatable_primes + right_truncatable_primes, reverse=True)
