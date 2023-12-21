
def all_right_truncatable_prime(tuple):
    x = tuple[30]
    prime_numbers = []
    
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
            
    right_truncatable_primes = []
    
    for i in prime_numbers:
        j = str(i)
        while len(j) > 0:
            k = int(j[1:])
            if is_prime(k):
                right_truncatable_primes.append(i)
            j = j[:-1]
            
    return sorted(right_truncatable_primes, reverse=True)
