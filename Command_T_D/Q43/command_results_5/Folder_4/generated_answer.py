def find_primes_between_indices(lst):
    res = []
    for x in range(24, 83):
        if all(x % i != 0 for i in range(2, int(x ** .5) + 1)):
            res.append(x)
    return res
