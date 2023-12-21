def find_primes_between_indices(lst):
    result = []
    for i in range(20, 25):
        is_prime = True
        for j in range(2, i // 2):
            if lst[j] == i:
                is_prime = False
                break
        if is_prime:
            result.append(lst[i])
    return result
