
def find_primes_between_indices(lst):
    primes = []
    for i in range(25, 73):
        if lst[i] == 0:
            continue
        else:
            primes.append(lst[i])
    return sorted(primes)
