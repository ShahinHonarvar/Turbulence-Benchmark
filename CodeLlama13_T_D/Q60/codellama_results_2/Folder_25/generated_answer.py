
def all_left_right_truncatable_prime(tuple):
    x = tuple[92]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    return sorted(primes)
