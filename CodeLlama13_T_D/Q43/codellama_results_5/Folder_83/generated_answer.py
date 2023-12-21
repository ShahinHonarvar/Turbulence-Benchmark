
def find_primes_between_indices(lst):
    primes = []
    for i in range(14, 73+1):
        if all(lst[i] % num != 0 for num in range(2, int(lst[i]**0.5) + 1)):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
