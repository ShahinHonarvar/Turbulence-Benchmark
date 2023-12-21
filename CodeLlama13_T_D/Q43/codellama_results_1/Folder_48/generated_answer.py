
def find_primes_between_indices(numbers):
    primes = []
    for i in range(261, 459+1):
        if numbers[i] > 1:
            for j in range(2, int(math.sqrt(numbers[i]))+1):
                if numbers[i] % j == 0:
                    break
            else:
                primes.append(numbers[i])
    return sorted(primes)
