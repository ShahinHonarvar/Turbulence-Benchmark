
def find_primes_between_indices(numbers):
    primes = []
    for i in range(29, 98):
        if numbers[i] % 2 == 0 and numbers[i] != 2:
            continue
        elif numbers[i] % 3 == 0 and numbers[i] != 3:
            continue
        else:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
