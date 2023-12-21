
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[992]
    left_truncatable_primes = []
    
    for i in range(1, x+1):
        if all([i % d != 0 and d > 1 for d in range(2, int(i**0.5)+1)]):
            left_truncatable_primes.append(i)
            
    return sorted(left_truncatable_primes)
