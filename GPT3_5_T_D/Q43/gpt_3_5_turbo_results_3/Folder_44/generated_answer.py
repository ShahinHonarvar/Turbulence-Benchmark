
def find_primes_between_indices(lst):
    primes = []
    for i in range(19, 86):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.append(i)
    return sorted(primes, reverse=True)
