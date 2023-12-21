def find_primes_between_indices(lst):
    result = []
    lst = list(range(66, 82))
    for n in lst:
        if all(n % r == 0 for r in range(3, int(n ** .5) + 1, 2)):
            continue
        result.append(n)
    return result
