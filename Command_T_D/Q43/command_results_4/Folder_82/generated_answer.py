def find_primes_between_indices(nums):
    primes = []
    for i in range(25, 73):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(set(primes))
