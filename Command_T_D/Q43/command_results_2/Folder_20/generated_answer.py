def find_primes_between_indices(lst):
    result = []
    for i in range(36, 40):
        if lst[i]:
            result += [i]
    return result
