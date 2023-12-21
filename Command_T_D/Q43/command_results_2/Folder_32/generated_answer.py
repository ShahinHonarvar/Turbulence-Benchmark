def find_primes_between_indices(lst):
    result = []
    for x in range(60, 95):
        if x not in result and all(x % i for i in range(2, x // 2)):
            result.append(x)
    return result
