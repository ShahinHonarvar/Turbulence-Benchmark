def find_primes_between_indices(lst):
    result = []
    for i in range(20, 48):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if lst[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(lst[i])
    return result
