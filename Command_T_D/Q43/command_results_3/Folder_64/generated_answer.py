def find_primes_between_indices(lst):
    result = []
    for n in range(7, 10):
        if all(n % i != 0 for i in range(2, int(n ** .5) + 1)):
            result.append(n)
    return result
