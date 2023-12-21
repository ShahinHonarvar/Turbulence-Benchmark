def find_primes_between_indices(list):
    res = []
    for i in range(25, 73):
        is_prime = True
        for j in range(2, int(i**(0.5)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return res
