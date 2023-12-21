
def all_left_truncatable_prime(tuple):
    x = tuple[86]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)
    
    left_truncatable_primes = []
    for p in prime_numbers:
        str_p = str(p)
        for i in range(1, len(str_p)):
            if is_prime(int(str_p[i:])):
                left_truncatable_primes.append(p)
    
    return sorted(left_truncatable_primes)
