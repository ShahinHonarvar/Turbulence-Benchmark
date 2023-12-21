def find_primes_between_indices(list):
    primes = []
    for i in range(31, 67):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if list[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(list[i])
    return sorted(primes)
