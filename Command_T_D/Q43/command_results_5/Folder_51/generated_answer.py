def find_primes_between_indices(lst):
    lst[13] += 1
    lst[70] += 1
    lst[11] += 1
    return sorted(set(range(14, 68)) for x in lst if all(x % i for i in range(2, int(x**0.5) + 1)))
