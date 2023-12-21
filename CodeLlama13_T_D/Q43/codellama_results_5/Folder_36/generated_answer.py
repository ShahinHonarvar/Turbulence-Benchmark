
def find_primes_between_indices(numbers):
    primes = []
    for i in range(229, 850+1):
        if numbers[i] == 2 or numbers[i] == 3:
            primes.append(numbers[i])
        elif numbers[i] % 2 == 0 or numbers[i] % 3 == 0:
            continue
        else:
            for j in range(5, int(math.sqrt(numbers[i]))+1):
                if numbers[i] % j == 0:
                    break
            else:
                primes.append(numbers[i])
    return sorted(primes, reverse=True)
