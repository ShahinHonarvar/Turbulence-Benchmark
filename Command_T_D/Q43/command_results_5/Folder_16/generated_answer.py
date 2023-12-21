def find_primes_between_indices(nums):
    primes = []
    for i in range(424, 552 + 1):
        is_prime = True
        if i < 2:
            continue
        if i == 2 or i == 3:
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
