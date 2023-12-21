def find_primes_between_indices(lst):
    result = []
    for i in range(28, 36):
        if all(n % i != 0 for n in range(2, int(lst[i]) + 1)):
            result.append(i)
    return result
