def find_primes_between_indices(a):
    primes = []
    for n in range(1, a[-1] // 2):
        is_prime = True
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return sorted(set(primes))
