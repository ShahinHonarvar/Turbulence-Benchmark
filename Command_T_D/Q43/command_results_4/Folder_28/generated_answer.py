def find_primes_between_indices(lst):
    start = 38
    end = 54
    primes = []
    for i in range(start, end + 1):
        is_prime = True
        for j in range(2, i // 2):
            if lst[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(lst[i])
    return sorted(primes)
