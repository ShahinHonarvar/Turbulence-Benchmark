def all_right_truncatable_prime(x):
    #Create list of all prime numbers less than x
    primes = []
    for i in range(2, x+1):
        is_prime = True
        #Check for divisibility by all prime numbers
        for j in range(2, int(str(i)[-1])+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    #Filter to only right-truncatable primes
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable = True
        #Check for divisibility by all prime numbers
        for j in range(2, int(str(prime)[-1])+1):
            if prime % j == 0:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    #Sort in descending order
    return sorted(right_truncatable_primes, reverse=True)
