
def find_primes_between_indices(numbers):
    primes = []
    for i in range(7, 10):
        if numbers[i] == 0:
            continue
        is_prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
