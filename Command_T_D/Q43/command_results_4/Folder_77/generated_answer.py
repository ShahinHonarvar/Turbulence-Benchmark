def find_primes_between_indices(lst):
    res = []
    for idx in range(287, 928):
        is_prime = True
        for i in range(2, idx // 2):
            if idx % i == 0:
                is_prime = False
                break
        if is_prime:
            res.append(idx)
    return res
