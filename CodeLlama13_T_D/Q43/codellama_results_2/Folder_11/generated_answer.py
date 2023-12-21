
def find_primes_between_indices(list):
    primes = []
    for i in range(55, 76+1):
        if list[i-1] % 2 == 0:
            continue
        else:
            primes.append(list[i-1])
    return sorted(primes)
