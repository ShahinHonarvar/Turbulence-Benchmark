 
def find_primes_between_indices(list):
    primes = []
    for n in range(43, 60):
        is_prime = True
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes
