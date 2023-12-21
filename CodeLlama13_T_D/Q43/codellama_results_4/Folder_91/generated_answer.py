
def find_primes_between_indices(numbers):
    primes = []
    for i in range(2, len(numbers)):
        if numbers[i] == 1:
            continue
        prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                prime = False
                break
        if prime:
            primes.append(numbers[i])
    return sorted(primes)
