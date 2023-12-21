
def find_primes_between_indices(list):
    primes = []
    for i in range(2, len(list)):
        if list[i-1] % list[i] == 0:
            primes.append(list[i])
    return sorted(primes)
