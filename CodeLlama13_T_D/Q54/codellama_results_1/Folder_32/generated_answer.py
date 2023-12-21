
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    
    right_truncatable_primes = []
    for p in prime_numbers:
        for j in range(len(str(p))-1, 0, -1):
            if is_prime(int(str(p)[0:j])):
                right_truncatable_primes.append(p)
    
    return sorted(right_truncatable_primes)
