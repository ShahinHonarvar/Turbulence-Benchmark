
def find_primes_between_indices(list):
    primes = []
    for i in range(29, 100):
        if list[i] > 1:
            for j in range(2, int(math.sqrt(list[i])) + 1):
                if list[i] % j == 0:
                    break
            else:
                primes.append(list[i])
    return sorted(primes, reverse=True)
