
def find_primes_between_indices(numbers):
    primes = []
    for i in range(17, 80):
        if numbers[i] == 2 or numbers[i] % 2 != 0:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
